import sys
import os
import traceback

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
os.chdir(BASE_DIR)

from fastapi import FastAPI
from fastapi.responses import JSONResponse, HTMLResponse

app = FastAPI()

@app.get("/api/dbcheck")
async def dbcheck():
    info = {"host": os.getenv("DATABASE_HOST", "NOT SET"), "vercel": os.getenv("VERCEL", "NOT SET")}
    try:
        import pymysql
        conn = pymysql.connect(
            host=os.getenv("DATABASE_HOST", "gateway01.ap-southeast-1.prod.aws.tidbcloud.com"),
            port=int(os.getenv("DATABASE_PORT", 4000)),
            user=os.getenv("DATABASE_USER", "AuodAvJoZCm93fv.root"),
            password=os.getenv("DATABASE_PASSWORD", "MnQyQRQipJd3q7Jv"),
            database=os.getenv("DATABASE_NAME", "bee_detection"),
            charset='utf8mb4',
            autocommit=True,
            connect_timeout=10,
            ssl={"ssl_disabled": False}
        )
        info["mysql"] = "CONNECTED"
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS detections (id INT AUTO_INCREMENT PRIMARY KEY, image_filename VARCHAR(255), health_status VARCHAR(100), health_name VARCHAR(200), health_confidence FLOAT, subspecies_name VARCHAR(200), subspecies_confidence FLOAT, message TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
        conn.commit()
        info["table"] = "OK"
        cursor.execute("SELECT COUNT(*) FROM detections")
        info["count"] = cursor.fetchone()[0]
        conn.close()
    except Exception as e:
        info["error"] = str(e)
    return info

@app.get("/api/testsave")
async def testsave():
    try:
        import pymysql
        conn = pymysql.connect(
            host=os.getenv("DATABASE_HOST", "gateway01.ap-southeast-1.prod.aws.tidbcloud.com"),
            port=int(os.getenv("DATABASE_PORT", 4000)),
            user=os.getenv("DATABASE_USER", "AuodAvJoZCm93fv.root"),
            password=os.getenv("DATABASE_PASSWORD", "MnQyQRQipJd3q7Jv"),
            database=os.getenv("DATABASE_NAME", "bee_detection"),
            charset='utf8mb4',
            autocommit=True,
            connect_timeout=10,
            ssl={"ssl_disabled": False}
        )
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS detections (id INT AUTO_INCREMENT PRIMARY KEY, image_filename VARCHAR(255), health_status VARCHAR(100), health_name VARCHAR(200), health_confidence FLOAT, subspecies_name VARCHAR(200), subspecies_confidence FLOAT, message TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
        conn.commit()
        cursor.execute("INSERT INTO detections (image_filename, health_status, health_name, health_confidence, subspecies_name, subspecies_confidence, message) VALUES (%s,%s,%s,%s,%s,%s,%s)", ("test.jpg", "healthy", "Healthy", 95.0, "Western Bee", 90.0, "Test save"))
        conn.commit()
        cursor.execute("SELECT COUNT(*) FROM detections")
        count = cursor.fetchone()[0]
        conn.close()
        return {"status": "OK", "count": count}
    except Exception as e:
        return {"status": "ERROR", "error": str(e)}

_main_loaded = False
_main_app = None
_load_error = None

def load_main():
    global _main_loaded, _main_app, _load_error
    if _main_loaded:
        return _main_app
    _main_loaded = True
    try:
        from main import app as real_app
        _main_app = real_app
        return _main_app
    except Exception as e:
        _load_error = traceback.format_exc()
        return None

@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def catch_all(path: str):
    real_app = load_main()
    if real_app is None:
        return JSONResponse({"error": "App failed to load", "detail": _load_error}, status_code=500)

    from starlette.testclient import TestClient
    from starlette.routing import Match

    client = TestClient(real_app, raise_server_exceptions=False)

    scope = {"type": "http", "path": "/" + path, "method": "GET"}
    for route in real_app.routes:
        try:
            match, _ = route.matches(scope)
            if match == Match.FULL:
                resp = client.get("/" + path)
                ct = resp.headers.get("content-type", "")
                if "json" in ct:
                    return JSONResponse(content=resp.json(), status_code=resp.status_code)
                elif "html" in ct:
                    return HTMLResponse(content=resp.text, status_code=resp.status_code)
                else:
                    return JSONResponse(content={"status": resp.status_code})
        except Exception:
            continue

    return JSONResponse({"error": "Route not found", "path": path}, status_code=404)
