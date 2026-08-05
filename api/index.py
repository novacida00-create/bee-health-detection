import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from main import app

from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

static_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

def handler(request, response):
    return app
