import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
os.chdir(BASE_DIR)

from main import app

@app.get("/api/debug")
async def debug():
    import onnxruntime as ort
    info = {
        "cwd": os.getcwd(),
        "base_dir": BASE_DIR,
        "files": os.listdir(BASE_DIR),
        "models_dir": os.listdir(os.path.join(BASE_DIR, "models")) if os.path.exists(os.path.join(BASE_DIR, "models")) else "NOT FOUND",
    }
    try:
        m1_path = os.path.join(BASE_DIR, "models", "model1.onnx")
        m2_path = os.path.join(BASE_DIR, "models", "model2.onnx")
        info["model1_exists"] = os.path.exists(m1_path)
        info["model2_exists"] = os.path.exists(m2_path)
        if os.path.exists(m1_path):
            info["model1_size"] = os.path.getsize(m1_path)
        sess = ort.InferenceSession(m1_path)
        info["onnx_ok"] = True
    except Exception as e:
        info["onnx_error"] = str(e)
    return info
