import os
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
