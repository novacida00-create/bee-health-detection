import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")
DATABASE_PORT = int(os.getenv("DATABASE_PORT", 3306))
DATABASE_USER = os.getenv("DATABASE_USER", "root")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "")
DATABASE_NAME = os.getenv("DATABASE_NAME", "bee_detection")

MODEL_DIR = os.path.join(os.path.dirname(__file__), "models")
MODEL1_PATH = os.path.join(MODEL_DIR, "best_model1.weights.h5")
MODEL2_PATH = os.path.join(MODEL_DIR, "best_model2.weights.h5")

UPLOAD_DIR = os.path.join(os.path.dirname(__file__), "static", "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

IMG_WIDTH = 100
IMG_HEIGHT = 100
IMG_CHANNELS = 3

CLASS_NAMES_SUBSPECIES = [
    "-1",
    "1 Mixed Local Stock 2",
    "Carniolan Honey Bee",
    "Italian Honey Bee",
    "Russian Honey Bee",
    "VSH Italian Honey Bee",
    "Western Honey Bee",
]

CLASS_NAMES_HEALTH = [
    "Varroa, Small Hive Beetles",
    "Ant Problems",
    "Few Varroa, Hive Beetles",
    "Healthy",
    "Hive Being Robbed",
    "Missing Queen",
]
