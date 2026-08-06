import sys
import os
import traceback

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
os.chdir(BASE_DIR)

try:
    from main import app
except Exception as e:
    from fastapi import FastAPI
    from fastapi.responses import JSONResponse
    app = FastAPI()

    @app.get("/api/error")
    async def error():
        return {"error": str(e), "trace": traceback.format_exc()}
