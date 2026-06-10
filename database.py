import sqlite3


conn = sqlite3.connect(
    "career_guidance.db"
)

cursor = conn.cursor()


# Users Table

cursor.execute("""

CREATE TABLE IF NOT EXISTS users (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    username TEXT UNIQUE,

    email TEXT UNIQUE,

    password TEXT

)

""")


# Resume Analysis Table

cursor.execute("""

CREATE TABLE IF NOT EXISTS analyses (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id INTEGER,

    filename TEXT,

    predicted_career TEXT,

    career_score INTEGER,

    resume_score INTEGER,

    skills TEXT,

    FOREIGN KEY(user_id)
    REFERENCES users(id)

)

""")


conn.commit()

conn.close()

print("Database Created Successfully")