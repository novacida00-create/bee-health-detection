import os

TIDB_HOST = "gateway01.ap-southeast-1.prod.aws.tidbcloud.com"
TIDB_PORT = 4000
TIDB_USER = "AuodAvJoZCm93fv.root"
TIDB_PASS = "aOjbLSoCFwYo0OZe"
TIDB_DB = "bee_detection"

def get_db_connection():
    db_host = os.getenv("DATABASE_HOST", TIDB_HOST)
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
        conn = pymysql.connect(
            host=os.getenv("DATABASE_HOST", TIDB_HOST),
            port=int(os.getenv("DATABASE_PORT", TIDB_PORT)),
            user=os.getenv("DATABASE_USER", TIDB_USER),
            password=os.getenv("DATABASE_PASSWORD", TIDB_PASS),
            database=os.getenv("DATABASE_NAME", TIDB_DB),
            charset='utf8mb4',
            autocommit=True,
            connect_timeout=10,
            ssl={"ssl_disabled": False}
        )
        print("[OK] MySQL connected!")
        return conn
    except Exception as e:
        print("[ERROR] MySQL: {}".format(e))
        return None
