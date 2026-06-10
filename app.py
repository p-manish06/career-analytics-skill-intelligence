from utils.db_manager import fetch_history
from utils.db_manager import save_to_database
from utils.pdf_generator import generate_pdf_report
from utils.resume_scorer import calculate_resume_score
from utils.ml_predictor import predict_career
from utils.learning_recommender import get_learning_recommendations
from utils.chart_generator import generate_chart
from utils.career_recommender import (
    recommend_career,
    get_strength_career,
    get_alternative_career

)
from utils.skill_gap_analyzer import analyze_skill_gap
from utils.skill_extractor import extract_skills
from flask import (

    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash

)

import sqlite3

from werkzeug.security import (

    generate_password_hash,

    check_password_hash

)

import os
import database

from utils.resume_parser import extract_text_from_pdf

app = Flask(__name__)
app.secret_key = "supersecretkey"

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/')

def home():

    if 'user_id' not in session:

        return redirect('/login')

    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_resume():

    if 'resume' not in request.files:

        return "No File Uploaded"

    file = request.files['resume']

    if file.filename == '':

        return "No Selected File"

    filepath = os.path.join(
        app.config['UPLOAD_FOLDER'],
        file.filename
    )
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    file.save(filepath)

    extracted_text = extract_text_from_pdf(filepath)
    skills = extract_skills(extracted_text)
    analysis = analyze_skill_gap(skills)
    recommended_career, career_score = recommend_career(analysis)
    alternative_career, alternative_score = get_alternative_career(
    analysis,
    recommended_career)

    strength_career, missing_count = get_strength_career(analysis)
    chart_path = generate_chart(analysis)
    recommendations = get_learning_recommendations(analysis)
    resume_score, feedback = calculate_resume_score(
    skills,
    career_score,
    extracted_text
    )

    pdf_path = generate_pdf_report(

    recommended_career,
    career_score,
    resume_score,
    skills,
    analysis,
    feedback
    )
    skills_text = ", ".join(skills)

    save_to_database(

    session['user_id'],

    file.filename,

    recommended_career,

    career_score,

    resume_score,

    skills_text

)

    return render_template(
    'result.html',
    text=extracted_text,
    skills=skills,
    analysis=analysis,
    recommended_career=recommended_career,
    career_score=career_score,
    chart_path=chart_path,
    resume_score=resume_score,
    feedback=feedback,
    recommendations=recommendations,
    pdf_path=pdf_path,
    strength_career=strength_career,
    alternative_career=alternative_career,
    alternative_score=alternative_score,
    missing_count=missing_count
)

@app.route('/history')

def history():

    if 'user_id' not in session:

        return redirect('/login')

    rows = fetch_history(

        session['user_id']

    )

    return render_template(

        'history.html',

        rows=rows

    )


@app.route('/signup', methods=['GET', 'POST'])

def signup():

    if request.method == 'POST':

        username = request.form.get(

            'username', ''

        ).strip()

        email = request.form.get(

            'email', ''

        ).strip()

        password = request.form.get(

            'password', ''

        ).strip()

        confirm_password = request.form.get(

            'confirm_password', ''

        ).strip()

        if (

            not username or

            not email or

            not password or

            not confirm_password

        ):

            flash(

                "Please fill all fields.",

                "warning"

            )

            return render_template(

                'signup.html',

                username=username,

                email=email

            )

        if '@' not in email:

            flash(

                "Invalid email format.",

                "danger"

            )

            return render_template(

                'signup.html',

                username=username,

                email=email

            )

        if password != confirm_password:

            flash(

                "Passwords do not match.",

                "danger"

            )

            return render_template(

                'signup.html',

                username=username,

                email=email

            )

        hashed_password = generate_password_hash(

            password

        )

        conn = sqlite3.connect(

            "career_guidance.db"

        )

        cursor = conn.cursor()

        try:

            cursor.execute("""

            INSERT INTO users (

                username,
                email,
                password

            )

            VALUES (?, ?, ?)

            """, (

                username,
                email,
                hashed_password

            ))

            conn.commit()

            conn.close()

            flash(

                "Signup successful! Please login.",

                "success"

            )

            return redirect('/login')

        except sqlite3.IntegrityError:

            flash(

                "User already exists.",

                "danger"

            )

            conn.close()

            return render_template(

                'signup.html',

                username=username,

                email=email

            )

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])

def login():

    if request.method == 'POST':

        email = request.form.get('email', '').strip()

        password = request.form.get('password', '').strip()

        if not email or not password:

            flash(

                "Please fill all fields.",

                "warning"

            )

            return render_template(

                'login.html',

                email=email

            )

        conn = sqlite3.connect(

            "career_guidance.db"

        )

        cursor = conn.cursor()

        cursor.execute("""

        SELECT id, password

        FROM users

        WHERE email=?

        """, (email,))

        user = cursor.fetchone()

        conn.close()

        if not user:

            flash(

                "Account not found. Please sign up first.",

                "danger"

            )

            return render_template(

                'login.html',

                email=email

            )

        if not check_password_hash(

            user[1],

            password

        ):

            flash(

                "Incorrect password. Please try again.",

                "danger"

            )

            return render_template(

                'login.html',

                email=email

            )

        session['user_id'] = user[0]

        flash(

            "Login successful!",

            "success"

        )

        return redirect('/')

    return render_template('login.html')

@app.route('/logout')

def logout():

    session.clear()

    flash("Logged Out")

    return redirect('/login')
if __name__ == "__main__":

    app.run()