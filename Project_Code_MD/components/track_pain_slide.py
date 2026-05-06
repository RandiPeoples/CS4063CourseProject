import sqlite3

def get_db():
    conn = sqlite3.connect("app_data.db")
    return conn, conn.cursor()

def init_db():
    conn, cur = get_db()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS symptoms (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        severity INTEGER,
        notes TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()