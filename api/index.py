import sys
import os
import traceback

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
os.chdir(BASE_DIR)

from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"status": "ok", "cwd": os.getcwd()}

@app.get("/api/debug")
async def debug():
    info = {"cwd": os.getcwd(), "base": BASE_DIR}
    try:
        info["base_files"] = os.listdir(BASE_DIR)
    except:
        pass
    try:
        info["models"] = os.listdir(os.path.join(BASE_DIR, "models"))
    except Exception as e:
        info["models_err"] = str(e)
    try:
        import onnxruntime
        info["onnxruntime"] = "OK"
    except Exception as e:
        info["onnxruntime"] = str(e)
    try:
        import pymysql
        info["pymysql"] = "OK"
    except Exception as e:
        info["pymysql"] = str(e)
    try:
        from main import app as main_app
        info["main_import"] = "OK"
    except Exception as e:
        info["main_import"] = str(e)
        info["main_trace"] = traceback.format_exc()
    return info
