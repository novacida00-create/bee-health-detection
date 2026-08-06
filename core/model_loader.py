import os
import numpy as np
from PIL import Image
from config import MODEL1_PATH, MODEL2_PATH, IMG_WIDTH, IMG_HEIGHT, IMG_CHANNELS

_session1 = None
_session2 = None

def load_models():
    import onnxruntime as ort
    global _session1, _session2

    model1_onnx = os.path.join(os.path.dirname(MODEL1_PATH), "model1.onnx")
    model2_onnx = os.path.join(os.path.dirname(MODEL2_PATH), "model2.onnx")

    if not os.path.exists(model1_onnx):
        raise FileNotFoundError(f"Model 1 not found: {model1_onnx}")
    if not os.path.exists(model2_onnx):
        raise FileNotFoundError(f"Model 2 not found: {model2_onnx}")

    opts = ort.SessionOptions()
    opts.inter_op_num_threads = 1
    opts.intra_op_num_threads = 1
    opts.log_severity_level = 3

    _session1 = ort.InferenceSession(model1_onnx, opts)
    _session2 = ort.InferenceSession(model2_onnx, opts)
    print("[OK] ONNX models loaded successfully!")

def get_model1():
    if _session1 is None:
        load_models()
    return _session1

def get_model2():
    if _session2 is None:
        load_models()
    return _session2
