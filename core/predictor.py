import numpy as np
from PIL import Image
from config import IMG_WIDTH, IMG_HEIGHT, IMG_CHANNELS, CLASS_NAMES_SUBSPECIES, CLASS_NAMES_HEALTH
from core.model_loader import get_model1, get_model2
from core.disease_database import get_disease_info

def preprocess_image(image_bytes: bytes) -> np.ndarray:
    image = Image.open(image_bytes).convert("RGB")
    image = image.resize((IMG_WIDTH, IMG_HEIGHT))
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def predict(image_bytes: bytes) -> dict:
    img_array = preprocess_image(image_bytes)

    model1 = get_model1()
    model2 = get_model2()

    pred_subspecies = model1.predict(img_array, verbose=0)
    pred_health = model2.predict(img_array, verbose=0)

    subspecies_idx = int(np.argmax(pred_subspecies[0]))
    health_idx = int(np.argmax(pred_health[0]))

    subspecies_name = CLASS_NAMES_SUBSPECIES[subspecies_idx]
    health_name = CLASS_NAMES_HEALTH[health_idx]

    subspecies_confidence = float(pred_subspecies[0][subspecies_idx])
    health_confidence = float(pred_health[0][health_idx])

    disease_info = get_disease_info(health_name)

    return {
        "subspecies": {
            "name": subspecies_name,
            "confidence": round(subspecies_confidence * 100, 2),
            "index": subspecies_idx
        },
        "health": {
            "name": health_name,
            "name_id": disease_info.get("name_id", health_name),
            "status": disease_info.get("status", "healthy"),
            "confidence": round(health_confidence * 100, 2),
            "index": health_idx
        },
        "disease_info": disease_info,
        "message": build_result_message(health_name, disease_info)
    }

def build_result_message(health_name: str, disease_info: dict) -> str:
    status = disease_info.get("status", "healthy")
    name_id = disease_info.get("name_id", health_name)
    madu_status = disease_info.get("madu_status", "AMAN")

    if status == "healthy":
        return f"✅ Lebah ini SEHAT - Madu yang dihasilkan AMAN untuk konsumsi"
    elif status == "warning":
        return f"⚠️ Lebah memiliki {name_id} - Madu perlu HATI-HATI sebelum dikonsumsi"
    else:
        return f"❌ Lebah terinfeksi {name_id} - Madu TIDAK AMAN untuk konsumsi"
