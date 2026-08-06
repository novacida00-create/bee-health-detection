import os

def get_db_connection():
    db_host = os.getenv("DATABASE_HOST")
    if db_host:
        return get_mysql_connection()
    return get_sqlite_connection()

def get_sqlite_connection():
    import sqlite3
    db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "bee_detection.db")
    try:
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        return conn
    except Exception as e:
        print("[ERROR] SQLite: {}".format(e))
        return None

def get_mysql_connection():
    try:
        import pymysql
        use_ssl = os.getenv("DATABASE_SSL", "false").lower() == "true"
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
        print("[ERROR] MySQL: {}".format(e))
        return get_sqlite_connection()
