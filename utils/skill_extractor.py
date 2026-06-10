import spacy

nlp = spacy.load("en_core_web_sm")

skills_list = [

    # Programming Languages

    "python",
    "java",
    "c",
    "c++",
    "c#",
    "javascript",
    "typescript",
    "php",
    "ruby",
    "swift",
    "kotlin",
    "go",
    "rust",
    "r",
    "matlab",
    "scala",
    "perl",
    "dart",


    # Web Development

    "html",
    "css",
    "bootstrap",
    "tailwind",
    "react",
    "angular",
    "vue",
    "next.js",
    "node.js",
    "express.js",
    "flask",
    "django",
    "fastapi",
    "jquery",
    "ajax",
    "rest api",
    "graphql",


    # Databases

    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "sqlite",
    "oracle",
    "firebase",
    "redis",
    "cassandra",
    "dynamodb",


    # Data Science

    "numpy",
    "pandas",
    "matplotlib",
    "seaborn",
    "plotly",
    "power bi",
    "tableau",
    "excel",
    "data analysis",
    "data visualization",
    "statistics",
    "probability",
    "data cleaning",
    "feature engineering",
    "business analytics",


    # Machine Learning

    "machine learning",
    "deep learning",
    "artificial intelligence",
    "nlp",
    "computer vision",
    "tensorflow",
    "keras",
    "pytorch",
    "scikit-learn",
    "xgboost",
    "cnn",
    "rnn",
    "lstm",
    "transformers",
    "opencv",
    "hugging face",
    "generative ai",
    "llm",
    "prompt engineering",


    # Cloud & DevOps

    "aws",
    "azure",
    "gcp",
    "docker",
    "kubernetes",
    "jenkins",
    "terraform",
    "ansible",
    "github actions",
    "linux",
    "bash",
    "shell scripting",
    "ci/cd",


    # Cybersecurity

    "network security",
    "ethical hacking",
    "penetration testing",
    "cryptography",
    "firewalls",
    "siem",
    "soc",
    "incident response",
    "vulnerability assessment",


    # Mobile Development

    "android",
    "flutter",
    "react native",
    "ios",
    "swiftui",


    # Software Engineering

    "oop",
    "data structures",
    "system design",
    "microservices",
    "design patterns",
    "multithreading",
    "api development",


    # Testing

    "unit testing",
    "selenium",
    "pytest",
    "junit",
    "automation testing",


    # Version Control

    "git",
    "github",
    "gitlab",
    "bitbucket",


    # Soft Skills

    "communication",
    "leadership",
    "teamwork",
    "problem solving",
    "critical thinking",
    "presentation",
    "time management",
    "collaboration",
    "adaptability",
    "creativity",


    # Business & Management

    "project management",
    "agile",
    "scrum",
    "jira",
    "product management",
    "business intelligence",
    "market research",


    # Tools & Platforms

    "vs code",
    "postman",
    "figma",
    "canva",
    "photoshop",
    "notion",


    # Emerging Technologies

    "blockchain",
    "iot",
    "robotics",
    "augmented reality",
    "virtual reality",
    "edge computing",
    "quantum computing",


    # Miscellaneous

    "resume writing",
    "technical writing",
    "public speaking",
    "customer support",
    "salesforce",
    "sap",
    "erp",
    "crm"
]


import re

def extract_skills(text):

    text = text.lower()

    doc = nlp(text)

    found_skills = set()

    tokens = [token.text for token in doc]

    for skill in skills_list:

        skill = skill.lower()

        # Single-word skills
        if len(skill.split()) == 1:

            if skill in tokens:

                found_skills.add(skill)

        # Multi-word skills
        else:

            pattern = r'\b' + re.escape(skill) + r'\b'

            if re.search(pattern, text):

                found_skills.add(skill)

    return list(found_skills)