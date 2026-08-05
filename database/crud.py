import os
import pymysql
from database.connection import get_db_connection
from config import DATABASE_HOST, DATABASE_PORT, DATABASE_USER, DATABASE_PASSWORD, DATABASE_NAME

def init_db():
    try:
        conn_check = pymysql.connect(
            host=DATABASE_HOST,
            port=DATABASE_PORT,
            user=DATABASE_USER,
            password=DATABASE_PASSWORD,
            charset='utf8mb4',
            autocommit=True,
            ssl={"ssl_disabled": False} if os.getenv("DATABASE_SSL", "false").lower() == "true" else None
        )
        cursor_check = conn_check.cursor()
        cursor_check.execute(f"CREATE DATABASE IF NOT EXISTS `{DATABASE_NAME}`")
        conn_check.close()
    except Exception as e:
        print(f"[WARN] Could not create database: {e}")

    conn = get_db_connection()
    if conn is None:
        print("[WARN] Could not connect to database. Running without database.")
        return
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS detections (
                id INT AUTO_INCREMENT PRIMARY KEY,
                image_filename VARCHAR(255) NOT NULL,
                health_status VARCHAR(100) NOT NULL,
                health_name VARCHAR(200) NOT NULL,
                health_confidence FLOAT NOT NULL,
                subspecies_name VARCHAR(200) NOT NULL,
                subspecies_confidence FLOAT NOT NULL,
                message TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        print("[OK] Database table initialized!")
    except Exception as e:
        print(f"[ERROR] Database init error: {e}")
    finally:
        conn.close()

def save_detection(image_filename, health_status, health_name, health_confidence, subspecies_name, subspecies_confidence, message):
    conn = get_db_connection()
    if conn is None:
        return None
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO detections (image_filename, health_status, health_name, health_confidence, subspecies_name, subspecies_confidence, message)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (image_filename, health_status, health_name, health_confidence, subspecies_name, subspecies_confidence, message))
        conn.commit()
        last_id = cursor.lastrowid
        return last_id
    except Exception as e:
        print(f"[ERROR] Database save error: {e}")
        return None
    finally:
        conn.close()

def get_all_detections():
    conn = get_db_connection()
    if conn is None:
        return []
    try:
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM detections ORDER BY created_at DESC")
        return cursor.fetchall()
    except Exception as e:
        print(f"[ERROR] Database fetch error: {e}")
        return []
    finally:
        conn.close()

def get_detection_by_id(detection_id):
    conn = get_db_connection()
    if conn is None:
        return None
    try:
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM detections WHERE id = %s", (detection_id,))
        return cursor.fetchone()
    except Exception as e:
        print(f"[ERROR] Database fetch error: {e}")
        return None
    finally:
        conn.close()

def delete_detection(detection_id):
    conn = get_db_connection()
    if conn is None:
        return False
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM detections WHERE id = %s", (detection_id,))
        conn.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"[ERROR] Database delete error: {e}")
        return False
    finally:
        conn.close()

def get_stats():
    conn = get_db_connection()
    if conn is None:
        return {"total": 0, "healthy": 0, "sick": 0, "warning": 0}
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM detections")
        total = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM detections WHERE health_status = 'healthy'")
        healthy = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM detections WHERE health_status = 'warning'")
        warning = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM detections WHERE health_status = 'danger'")
        sick = cursor.fetchone()[0]
        return {"total": total, "healthy": healthy, "sick": sick, "warning": warning}
    except Exception as e:
        print(f"[ERROR] Database stats error: {e}")
        return {"total": 0, "healthy": 0, "sick": 0, "warning": 0}
    finally:
        conn.close()
