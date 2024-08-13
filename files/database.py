import sqlite3 as sq

db = sq.connect("database.db")
cur = db.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER UNIQUE,
        limit_request INTEGER,
        lang TEXT
    )
""")
db.commit()