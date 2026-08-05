from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from database.crud import get_all_detections, delete_detection

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/api/history")
async def api_history():
    detections = get_all_detections()
    return {"success": True, "data": detections}

@router.delete("/api/history/{detection_id}")
async def api_delete_history(detection_id: int):
    success = delete_detection(detection_id)
    return {"success": success}

@router.get("/history", response_class=HTMLResponse)
async def history_page(request: Request):
    detections = get_all_detections()
    return templates.TemplateResponse("history.html", {
        "request": request,
        "detections": detections
    })
