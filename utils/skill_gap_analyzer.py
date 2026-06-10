career_skill_map = {

    "Data Scientist": [

        "python",
        "sql",
        "machine learning",
        "deep learning",
        "numpy",
        "pandas",
        "statistics",
        "scikit-learn"
    ],

    "Data Analyst": [

        "python",
        "sql",
        "excel",
        "power bi",
        "tableau",
        "data analysis"
    ],

    "Machine Learning Engineer": [

        "python",
        "machine learning",
        "tensorflow",
        "pytorch",
        "scikit-learn"
    ],

    "AI Engineer": [

        "python",
        "deep learning",
        "nlp",
        "generative ai",
        "llms"
    ],

    "Frontend Developer": [

        "html",
        "css",
        "javascript",
        "react",
        "bootstrap"
    ],

    "Backend Developer": [

        "python",
        "django",
        "flask",
        "sql",
        "mongodb"
    ],

    "Full Stack Developer": [

        "html",
        "css",
        "javascript",
        "react",
        "node.js",
        "mongodb"
    ],

    "MERN Stack Developer": [

        "react",
        "node.js",
        "express",
        "mongodb",
        "javascript"
    ],

    "Software Engineer": [

        "java",
        "c++",
        "data structures",
        "algorithms",
        "git"
    ],

    "Cybersecurity Analyst": [

        "cybersecurity",
        "network security",
        "linux",
        "ethical hacking"
    ],

    "Cloud Engineer": [

        "aws",
        "azure",
        "docker",
        "kubernetes",
        "linux"
    ],

    "Business Analyst": [

        "excel",
        "sql",
        "power bi",
        "communication",
        "data analysis"
    ],

    "Android Developer": [

        "java",
        "android",
        "firebase"
    ],

    "Flutter Developer": [

        "flutter",
        "firebase",
        "dart"
    ]
}


def analyze_skill_gap(user_skills):

    results = {}

    for career, required_skills in career_skill_map.items():

        missing_skills = []

        for skill in required_skills:

            if skill not in user_skills:

                missing_skills.append(skill)

        matched = len(required_skills) - len(missing_skills)

        match_percentage = int(
            (matched / len(required_skills)) * 100
        )

        results[career] = {

            "match_percentage": match_percentage,
            "missing_skills": missing_skills
        }

    return results