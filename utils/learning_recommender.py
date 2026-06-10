learning_resources = {

    "python":
        "Learn Python Programming and Practice Projects",

    "sql":
        "Practice SQL Queries and Database Concepts",

    "machine learning":
        "Study Scikit-learn, Regression, Classification",
    "communication":
        "Improve Communication and Presentation Skills",

    "data analysis":
        "Learn Data Cleaning, Visualization, and Analysis Techniques",

    "deep learning":
        "Learn Neural Networks and TensorFlow",

    "data science":
        "Study Data Analysis, Visualization, Statistics",

    "numpy":
        "Learn NumPy Arrays and Numerical Computing",

    "pandas":
        "Practice DataFrames and Data Cleaning",

    "statistics":
        "Learn Probability and Statistical Analysis",

    "html":
        "Learn HTML Website Structure",

    "css":
        "Learn CSS Styling and Responsive Design",

    "javascript":
        "Learn JavaScript Fundamentals",

    "react":
        "Study React Components and Frontend Development",

    "node.js":
        "Learn Backend Development using Node.js",

    "mongodb":
        "Learn NoSQL Database Management",

    "power bi":
        "Practice Dashboard Creation in Power BI",

    "tableau":
        "Learn Data Visualization using Tableau",

    "aws":
        "Learn AWS Cloud Fundamentals",

    "azure":
        "Study Microsoft Azure Cloud Services",

    "docker":
        "Learn Containerization using Docker",

    "kubernetes":
        "Learn Kubernetes Orchestration",
    "scikit-learn":
        "Learn Machine Learning using Scikit-learn",

    "pytorch":
        "Study Deep Learning using PyTorch",

    "git":
        "Practice Git and GitHub Version Control",

    "github":
        "Learn GitHub Collaboration Workflow",

    "linux":
        "Learn Linux Command Line Basics",

    "algorithms":
        "Practice DSA and Algorithms",

    "data structures":
        "Study Arrays, Trees, Graphs, Linked Lists",

    "express":
        "Learn Express.js Backend Framework",

    "bootstrap":
        "Learn Responsive UI using Bootstrap",

    "tailwind":
        "Learn Tailwind CSS Framework",

    "dart":
        "Learn Dart Programming Language",

    "firebase":
        "Learn Firebase Backend Services",

    "ui ux":
        "Learn UI/UX Design Principles",

    "network security":
        "Study Networking and Security Concepts"
}


def get_learning_recommendations(analysis):

    recommendations = {}

    for career, details in analysis.items():

        missing = details["missing_skills"]

        resources = []

        for skill in missing:

            if skill in learning_resources:

                resources.append({

                    "skill": skill,

                    "resource":
                        learning_resources[skill]

                })

        recommendations[career] = resources

    return recommendations