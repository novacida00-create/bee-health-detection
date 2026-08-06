import os
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

from core.model_loader import load_models
from database.crud import init_db
from routes import detection, history, dashboard

app = FastAPI(title="Bee Health Detection", version="1.0.0")

app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

app.include_router(detection.router)
app.include_router(history.router)
app.include_router(dashboard.router)

@app.on_event("startup")
async def startup_event():
    print("[START] Starting Bee Health Detection System...")
    try:
        load_models()
    except Exception as e:
        print(f"[WARN] Model loading error: {e}")
    try:
        init_db()
    except Exception as e:
        print(f"[WARN] Database init error: {e}")
    print("[OK] System ready!")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/testsave")
async def testsave():
    from database.crud import save_detection
    result = save_detection("test.jpg", "healthy", "Healthy", 95.0, "Western Honey Bee", 90.0, "Test message")
    return {"saved_id": result}

@app.get("/api/dbcheck")
async def dbcheck():
    import os
    info = {
        "DATABASE_HOST": os.getenv("DATABASE_HOST", "NOT SET"),
        "DATABASE_PORT": os.getenv("DATABASE_PORT", "NOT SET"),
        "DATABASE_USER": os.getenv("DATABASE_USER", "NOT SET"),
        "DATABASE_PASSWORD": "SET" if os.getenv("DATABASE_PASSWORD") else "NOT SET",
        "DATABASE_NAME": os.getenv("DATABASE_NAME", "NOT SET"),
        "DATABASE_SSL": os.getenv("DATABASE_SSL", "NOT SET"),
    }
    from database.connection import get_db_connection
    conn = get_db_connection()
    if conn is None:
        info["connection"] = "FAILED"
        return info
    info["connection"] = "OK"
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM detections")
        info["detection_count"] = cursor.fetchone()[0]
    except Exception as e:
        info["query_error"] = str(e)
    conn.close()
    return info

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
