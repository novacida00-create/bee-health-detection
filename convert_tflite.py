import tensorflow as tf
import os

MODEL_DIR = os.path.join(os.path.dirname(__file__), "models")

def convert_to_tflite(h5_path, tflite_path):
    if not os.path.exists(h5_path):
        print(f"[SKIP] {h5_path} not found")
        return False

    try:
        model = tf.keras.models.load_model(h5_path)
        converter = tf.lite.TFLiteConverter.from_keras_model(model)
        tflite_model = converter.convert()

        with open(tflite_path, "wb") as f:
            f.write(tflite_model)

        size_mb = os.path.getsize(tflite_path) / (1024 * 1024)
        print(f"[OK] Converted: {os.path.basename(tflite_path)} ({size_mb:.2f} MB)")
        return True
    except Exception as e:
        print(f"[ERROR] Convert failed: {e}")
        return False

if __name__ == "__main__":
    print("Converting models to TFLite...")
    convert_to_tflite(
        os.path.join(MODEL_DIR, "best_model1.weights.h5"),
        os.path.join(MODEL_DIR, "model1.tflite")
    )
    convert_to_tflite(
        os.path.join(MODEL_DIR, "best_model2.weights.h5"),
        os.path.join(MODEL_DIR, "model2.tflite")
    )
    print("Done!")
