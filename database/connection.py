import os
import pymysql

DB_TYPE = os.getenv("DATABASE_TYPE", "sqlite")

def get_db_connection():
    if DB_TYPE == "sqlite" or not os.getenv("DATABASE_HOST"):
        return get_sqlite_connection()
    return get_mysql_connection()

def get_sqlite_connection():
    import sqlite3
    db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "bee_detection.db")
    try:
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        return conn
    except Exception as e:
        print(f"[ERROR] SQLite connection error: {e}")
        return None

def get_mysql_connection():
    use_ssl = os.getenv("DATABASE_SSL", "false").lower() == "true"
    try:
        conn = pymysql.connect(
            host=os.getenv("DATABASE_HOST"),
            port=int(os.getenv("DATABASE_PORT", 3306)),
            user=os.getenv("DATABASE_USER"),
            password=os.getenv("DATABASE_PASSWORD"),
            database=os.getenv("DATABASE_NAME", "bee_detection"),
            charset='utf8mb4',
            autocommit=True,
            ssl={"ssl_disabled": False} if use_ssl else None
        )
        return conn
    except Exception as e:
        print(f"[ERROR] MySQL connection error: {e}")
        return None
