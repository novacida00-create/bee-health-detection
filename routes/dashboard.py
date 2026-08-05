from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from database.crud import get_stats, get_all_detections

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/api/stats")
async def api_stats():
    stats = get_stats()
    return {"success": True, "data": stats}

@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard_page(request: Request):
    stats = get_stats()
    detections = get_all_detections()

    health_counts = {}
    for d in detections:
        name = d["health_name"]
        health_counts[name] = health_counts.get(name, 0) + 1

    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "stats": stats,
        "health_counts": health_counts,
        "detections": detections[:10]
    })
