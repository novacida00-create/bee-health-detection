import os
import pymysql
from config import DATABASE_HOST, DATABASE_PORT, DATABASE_USER, DATABASE_PASSWORD, DATABASE_NAME

def get_db_connection():
    use_ssl = os.getenv("DATABASE_SSL", "false").lower() == "true"
    ssl_config = {"ssl": {"ca": None}} if use_ssl else None

    try:
        conn = pymysql.connect(
            host=DATABASE_HOST,
            port=DATABASE_PORT,
            user=DATABASE_USER,
            password=DATABASE_PASSWORD,
            database=DATABASE_NAME,
            charset='utf8mb4',
            autocommit=True,
            ssl=ssl_config
        )
        return conn
    except pymysql.MySQLError as e:
        print(f"[ERROR] MySQL connection error: {e}")
        return None
    except Exception as e:
        print(f"[ERROR] Database connection error: {e}")
        return None
