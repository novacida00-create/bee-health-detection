import numpy as np
from PIL import Image
from config import (
    IMG_WIDTH,
    IMG_HEIGHT,
    IMG_CHANNELS,
    CLASS_NAMES_SUBSPECIES,
    CLASS_NAMES_HEALTH,
    CONFIDENCE_THRESHOLD,
    MARGIN_THRESHOLD,
)
from core.model_loader import get_model1, get_model2
from core.disease_database import get_disease_info

def preprocess_image(image_bytes: bytes) -> np.ndarray:
    image = Image.open(image_bytes).convert("RGB")
    image = image.resize((IMG_WIDTH, IMG_HEIGHT))
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array.astype(np.float32)

def predict(image_bytes: bytes) -> dict:
    img_array = preprocess_image(image_bytes)

    session1 = get_model1()
    session2 = get_model2()

    input_name1 = session1.get_inputs()[0].name
    input_name2 = session2.get_inputs()[0].name

    pred_subspecies = session1.run(None, {input_name1: img_array})[0]
    pred_health = session2.run(None, {input_name2: img_array})[0]

    subspecies_idx = int(np.argmax(pred_subspecies[0]))
    health_idx = int(np.argmax(pred_health[0]))

    subspecies_name = CLASS_NAMES_SUBSPECIES[subspecies_idx]
    health_name = CLASS_NAMES_HEALTH[health_idx]

    subspecies_confidence = float(pred_subspecies[0][subspecies_idx])
    health_confidence = float(pred_health[0][health_idx])

    subspecies_conf_pct = round(subspecies_confidence * 100, 2)
    health_conf_pct = round(health_confidence * 100, 2)

    sub_sorted = np.sort(pred_subspecies[0])
    health_sorted = np.sort(pred_health[0])
    sub_margin_pct = round(float(sub_sorted[-1] - sub_sorted[-2]) * 100, 2) if sub_sorted.size > 1 else 100.0
    health_margin_pct = round(float(health_sorted[-1] - health_sorted[-2]) * 100, 2) if health_sorted.size > 1 else 100.0

    if (
        subspecies_idx == 0
        or subspecies_conf_pct < CONFIDENCE_THRESHOLD
        or health_conf_pct < CONFIDENCE_THRESHOLD
        or sub_margin_pct < MARGIN_THRESHOLD
        or health_margin_pct < MARGIN_THRESHOLD
    ):
        return {
            "is_not_bee": True,
            "message": "Gambar tidak terdeteksi sebagai lebah madu. Sistem hanya mendeteksi foto lebah madu yang jelas. Silakan upload gambar lebah madu.",
            "subspecies": {
                "name": subspecies_name,
                "confidence": subspecies_conf_pct,
                "index": subspecies_idx
            },
            "health": {
                "name": health_name,
                "confidence": health_conf_pct,
                "index": health_idx
            }
        }

    disease_info = get_disease_info(health_name)

    return {
        "is_not_bee": False,
        "subspecies": {
            "name": subspecies_name,
            "confidence": subspecies_conf_pct,
            "index": subspecies_idx
        },
        "health": {
            "name": health_name,
            "name_id": disease_info.get("name_id", health_name),
            "status": disease_info.get("status", "healthy"),
            "confidence": health_conf_pct,
            "index": health_idx
        },
        "disease_info": disease_info,
        "message": build_result_message(health_name, disease_info)
    }

def build_result_message(health_name: str, disease_info: dict) -> str:
    status = disease_info.get("status", "healthy")
    name_id = disease_info.get("name_id", health_name)

    if status == "healthy":
        return "Lebah ini SEHAT - Madu yang dihasilkan AMAN untuk konsumsi"
    elif status == "warning":
        return "Lebah memiliki {} - Madu perlu HATI-HATI sebelum dikonsumsi".format(name_id)
    else:
        return "Lebah terinfeksi {} - Madu TIDAK AMAN untuk konsumsi".format(name_id)
