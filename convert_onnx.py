import tensorflow as tf
import tf2onnx
import os
import numpy as np

MODEL_DIR = os.path.join(os.path.dirname(__file__), "models")

def convert(h5_path, onnx_path, name):
    try:
        model = tf.keras.models.load_model(h5_path, compile=False)
        
        saved_model_dir = os.path.join(MODEL_DIR, f"temp_{name}")
        model.save(saved_model_dir)
        
        model_proto, _ = tf2onnx.convert.from_saved_model(
            saved_model_dir, 
            opset=13,
            input_signature=(tf.TensorSpec((None, 100, 100, 3), tf.float32, name="input_1"),)
        )
        with open(onnx_path, "wb") as f:
            f.write(model_proto.SerializeToString())
        
        import shutil
        shutil.rmtree(saved_model_dir, ignore_errors=True)
        
        size_mb = os.path.getsize(onnx_path) / (1024 * 1024)
        print(f"[OK] {name}: {size_mb:.2f} MB")
        return True
    except Exception as e:
        print(f"[ERROR] {name}: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    convert(os.path.join(MODEL_DIR, "best_model1.weights.h5"),
            os.path.join(MODEL_DIR, "model1.onnx"), "M1")
    convert(os.path.join(MODEL_DIR, "best_model2.weights.h5"),
            os.path.join(MODEL_DIR, "model2.onnx"), "M2")
