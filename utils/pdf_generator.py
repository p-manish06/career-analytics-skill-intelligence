from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.platypus import Spacer

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(

    recommended_career,
    career_score,
    resume_score,
    skills,
    analysis,
    feedback

):

    pdf_path = "static/report.pdf"

    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    elements = []

    # Title
    elements.append(

        Paragraph(
            "AI Career Analysis Report",
            styles['Title']
        )
    )

    elements.append(Spacer(1, 20))

    # Career Recommendation
    elements.append(

        Paragraph(
            f"<b>Recommended Career:</b> "
            f"{recommended_career}",
            styles['BodyText']
        )
    )

    elements.append(

        Paragraph(
            f"<b>Career Match Score:</b> "
            f"{career_score}%",
            styles['BodyText']
        )
    )

    elements.append(

        Paragraph(
            f"<b>ATS Resume Score:</b> "
            f"{resume_score}/100",
            styles['BodyText']
        )
    )

    elements.append(Spacer(1, 20))

    # Skills
    skills_text = ", ".join(skills)

    elements.append(

        Paragraph(
            f"<b>Detected Skills:</b> "
            f"{skills_text}",
            styles['BodyText']
        )
    )

    elements.append(Spacer(1, 20))

    # Feedback
    elements.append(

        Paragraph(
            "<b>Resume Feedback:</b>",
            styles['Heading2']
        )
    )

    for item in feedback:

        elements.append(

            Paragraph(
                f"• {item}",
                styles['BodyText']
            )
        )

    elements.append(Spacer(1, 20))

    # Skill Gap Analysis
    elements.append(

        Paragraph(
            "<b>Career Skill Gap Analysis:</b>",
            styles['Heading2']
        )
    )

    for career, details in analysis.items():

        missing = ", ".join(
            details["missing_skills"]
        )

        elements.append(

            Paragraph(
                f"<b>{career}</b> "
                f"({details['match_percentage']}%)",
                styles['BodyText']
            )
        )

        elements.append(

            Paragraph(
                f"Missing Skills: {missing}",
                styles['BodyText']
            )
        )

        elements.append(Spacer(1, 10))

    doc.build(elements)

    return pdf_path