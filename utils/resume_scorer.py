def calculate_resume_score(
    skills,
    career_score,
    text
):

    score = 0

    feedback = []

    # -----------------------------
    # Skill Score (40 Marks)
    # -----------------------------

    skill_score = min(len(skills) * 4, 40)

    score += skill_score

    if skill_score >= 30:

        feedback.append(
            "Strong technical skill set detected."
        )

    else:

        feedback.append(
            "Add more relevant technical skills."
        )

    # -----------------------------
    # Career Match Score (40 Marks)
    # -----------------------------

    career_points = int((career_score / 100) * 40)

    score += career_points

    if career_points >= 30:

        feedback.append(
            "Excellent career alignment."
        )

    else:

        feedback.append(
            "Resume needs better career-focused skills."
        )

    # -----------------------------
    # Resume Sections Score (20)
    # -----------------------------

    sections = [

        "education",
        "experience",
        "projects",
        "skills",
        "certifications"
    ]

    section_score = 0

    lower_text = text.lower()

    for section in sections:

        if section in lower_text:

            section_score += 4

    score += section_score

    if section_score >= 16:

        feedback.append(
            "Resume contains important sections."
        )

    else:

        feedback.append(
            "Add more resume sections like projects or certifications."
        )

    return score, feedback