import os
import numpy as np
from PIL import Image
from config import MODEL1_PATH, MODEL2_PATH, IMG_WIDTH, IMG_HEIGHT, IMG_CHANNELS

_model1 = None
_model2 = None

def load_models():
    global _model1, _model2
    import tensorflow as tf
    if not os.path.exists(MODEL1_PATH):
        raise FileNotFoundError(f"Model 1 not found: {MODEL1_PATH}")
    if not os.path.exists(MODEL2_PATH):
        raise FileNotFoundError(f"Model 2 not found: {MODEL2_PATH}")
    _model1 = tf.keras.models.load_model(MODEL1_PATH)
    _model2 = tf.keras.models.load_model(MODEL2_PATH)
    print("[OK] Models loaded successfully!")

def get_model1():
    if _model1 is None:
        load_models()
    return _model1

def get_model2():
    if _model2 is None:
        load_models()
    return _model2
