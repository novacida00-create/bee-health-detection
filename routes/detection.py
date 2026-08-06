import os
import uuid
import tempfile
from fastapi import APIRouter, UploadFile, File, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from core.predictor import predict
from database.crud import save_detection, get_detection_by_id
from config import UPLOAD_DIR

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

router = APIRouter()
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

@router.post("/api/predict")
async def api_predict(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        return {"success": False, "error": "File harus berupa gambar (JPG/PNG)"}

    contents = await file.read()

    ext = os.path.splitext(file.filename)[1]
    filename = f"{uuid.uuid4().hex}{ext}"

    try:
        filepath = os.path.join(UPLOAD_DIR, filename)
        with open(filepath, "wb") as f:
            f.write(contents)
    except Exception:
        filename = "unknown"

    from io import BytesIO
    image_bytes = BytesIO(contents)
    result = predict(image_bytes)

    detection_id = None
    save_error = None
    try:
        from database.crud import init_db
        init_db()
        detection_id = save_detection(
            image_filename=filename,
            health_status=result["health"]["status"],
            health_name=result["health"]["name"],
            health_confidence=result["health"]["confidence"],
            subspecies_name=result["subspecies"]["name"],
            subspecies_confidence=result["subspecies"]["confidence"],
            message=result["message"]
        )
    except Exception as e:
        save_error = str(e)
        print("[ERROR] Save detection failed: {}".format(e))

    result["id"] = detection_id
    result["image_url"] = f"/static/uploads/{filename}"
    return {"success": True, "data": result}

@router.get("/predict-page", response_class=HTMLResponse)
async def predict_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/result/{detection_id}", response_class=HTMLResponse)
async def result_page(request: Request, detection_id: int):
    detection = get_detection_by_id(detection_id)
    if not detection:
        return RedirectResponse(url="/", status_code=302)

    from core.disease_database import get_disease_info, DISEASE_DATABASE
    disease_info = get_disease_info(detection["health_name"])

    return templates.TemplateResponse("result.html", {
        "request": request,
        "detection": detection,
        "disease_info": disease_info
    })
