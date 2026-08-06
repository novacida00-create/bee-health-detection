import os

def get_db_connection():
    db_host = os.getenv("DATABASE_HOST")
    if db_host:
        conn = get_mysql_connection()
        if conn is not None:
            return conn
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
        ssl_args = {}
        if use_ssl:
            ssl_args = {"ssl": {"fake": True}}
        conn = pymysql.connect(
            host=os.getenv("DATABASE_HOST"),
            port=int(os.getenv("DATABASE_PORT", 3306)),
            user=os.getenv("DATABASE_USER"),
            password=os.getenv("DATABASE_PASSWORD"),
            database=os.getenv("DATABASE_NAME", "bee_detection"),
            charset='utf8mb4',
            autocommit=True,
            connect_timeout=10,
            ssl=ssl_args if ssl_args else None
        )
        print("[OK] MySQL connected!")
        return conn
    except Exception as e:
        print("[ERROR] MySQL: {}".format(e))
        return None
