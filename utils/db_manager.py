import sqlite3


# Save Analysis

def save_to_database(

    user_id,

    filename,

    predicted_career,

    career_score,

    resume_score,

    skills

):

    conn = sqlite3.connect(
        "career_guidance.db"
    )

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO analyses (

            user_id,
            filename,
            predicted_career,
            career_score,
            resume_score,
            skills

        )

        VALUES (?, ?, ?, ?, ?, ?)

    """, (

        user_id,
        filename,
        predicted_career,
        career_score,
        resume_score,
        skills

    ))

    conn.commit()

    conn.close()


# Fetch User History

def fetch_history(user_id):

    conn = sqlite3.connect(
        "career_guidance.db"
    )

    cursor = conn.cursor()

    cursor.execute("""

        SELECT

            filename,
            predicted_career,
            career_score,
            resume_score,
            skills

        FROM analyses

        WHERE user_id=?

        ORDER BY id DESC

    """, (user_id,))

    rows = cursor.fetchall()

    conn.close()

    return rows