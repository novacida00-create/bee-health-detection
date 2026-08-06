import os
from database.connection import get_db_connection

def _placeholder(conn):
    try:
        import pymysql
        if isinstance(conn, pymysql.connections.Connection):
            return "%s"
    except:
        pass
    return "?"

def init_db():
    db_host = os.getenv("DATABASE_HOST")
    if db_host:
        try:
            import pymysql
            use_ssl = os.getenv("DATABASE_SSL", "false").lower() == "true"
            conn_check = pymysql.connect(
                host=db_host,
                port=int(os.getenv("DATABASE_PORT", 3306)),
                user=os.getenv("DATABASE_USER"),
                password=os.getenv("DATABASE_PASSWORD"),
                charset='utf8mb4',
                autocommit=True,
                ssl={"ssl_disabled": False} if use_ssl else None
            )
            cursor_check = conn_check.cursor()
            db_name = os.getenv("DATABASE_NAME", "bee_detection")
            cursor_check.execute("CREATE DATABASE IF NOT EXISTS `{}`".format(db_name))
            conn_check.close()
        except Exception as e:
            print("[WARN] MySQL create db: {}".format(e))

    conn = get_db_connection()
    if conn is None:
        print("[WARN] No database connection.")
        return
    try:
        cursor = conn.cursor()
        p = _placeholder(conn)
        is_mysql = (p == "%s")
        if is_mysql:
            create_sql = """
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
            """
        else:
            create_sql = """
                CREATE TABLE IF NOT EXISTS detections (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    image_filename VARCHAR(255) NOT NULL,
                    health_status VARCHAR(100) NOT NULL,
                    health_name VARCHAR(200) NOT NULL,
                    health_confidence REAL NOT NULL,
                    subspecies_name VARCHAR(200) NOT NULL,
                    subspecies_confidence REAL NOT NULL,
                    message TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """
        cursor.execute(create_sql)
        try:
            cursor.execute("ALTER TABLE detections ADD COLUMN image_base64 LONGTEXT")
            conn.commit()
        except Exception:
            pass
        print("[OK] Database table initialized!")
    except Exception as e:
        print("[ERROR] DB init: {}".format(e))
    finally:
        conn.close()

def save_detection(image_filename, health_status, health_name, health_confidence, subspecies_name, subspecies_confidence, message, image_base64=None):
    conn = get_db_connection()
    if conn is None:
        return None
    try:
        p = _placeholder(conn)
        cursor = conn.cursor()
        sql = "INSERT INTO detections (image_filename, health_status, health_name, health_confidence, subspecies_name, subspecies_confidence, message, image_base64) VALUES ({0},{1},{2},{3},{4},{5},{6},{7})".format(p, p, p, p, p, p, p, p)
        cursor.execute(sql, (image_filename, health_status, health_name, health_confidence, subspecies_name, subspecies_confidence, message, image_base64))
        conn.commit()
        last_id = cursor.lastrowid
        return last_id
    except Exception as e:
        print("[ERROR] DB save: {}".format(e))
        return None
    finally:
        conn.close()

def get_all_detections():
    conn = get_db_connection()
    if conn is None:
        return []
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM detections ORDER BY created_at DESC")
        columns = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        return [dict(zip(columns, row)) for row in rows]
    except Exception as e:
        print("[ERROR] DB fetch: {}".format(e))
        return []
    finally:
        conn.close()

def get_detection_by_id(detection_id):
    conn = get_db_connection()
    if conn is None:
        return None
    try:
        p = _placeholder(conn)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM detections WHERE id = {}".format(p), (detection_id,))
        row = cursor.fetchone()
        if row:
            columns = [desc[0] for desc in cursor.description]
            return dict(zip(columns, row))
        return None
    except Exception as e:
        print("[ERROR] DB fetch: {}".format(e))
        return None
    finally:
        conn.close()

def delete_detection(detection_id):
    conn = get_db_connection()
    if conn is None:
        return False
    try:
        p = _placeholder(conn)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM detections WHERE id = {}".format(p), (detection_id,))
        conn.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print("[ERROR] DB delete: {}".format(e))
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
        print("[ERROR] DB stats: {}".format(e))
        return {"total": 0, "healthy": 0, "sick": 0, "warning": 0}
    finally:
        conn.close()
