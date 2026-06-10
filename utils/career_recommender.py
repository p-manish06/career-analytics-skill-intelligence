def recommend_career(analysis):

    best_career = None

    highest_match = 0

    for career, details in analysis.items():

        if details["match_percentage"] > highest_match:

            highest_match = details["match_percentage"]

            best_career = career

    return best_career, highest_match

def get_strength_career(analysis):

    best_career = None
    min_missing = float('inf')

    for career, details in analysis.items():

        missing_count = len(details["missing_skills"])

        if missing_count < min_missing:

            min_missing = missing_count
            best_career = career

    return best_career, min_missing

def get_alternative_career(analysis, recommended_career):

    sorted_careers = sorted(
        analysis.items(),
        key=lambda x: x[1]["match_percentage"],
        reverse=True
    )

    for career, details in sorted_careers:

        if career != recommended_career:

            return career, details["match_percentage"]

    return None, 0