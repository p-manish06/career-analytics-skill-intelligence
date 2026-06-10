import matplotlib.pyplot as plt


def generate_chart(analysis):

    careers = []
    percentages = []

    for career, details in analysis.items():

        careers.append(career)

        percentages.append(details["match_percentage"])

    plt.figure(figsize=(14,7))

    bars = plt.bar(careers, percentages)

    plt.xlabel("Career Paths", fontsize=12)

    plt.ylabel("Match Percentage", fontsize=12)

    plt.title(
        "Career Match Analysis",
        fontsize=18,
        fontweight='bold'
    )

    plt.ylim(0,100)

    plt.xticks(rotation=30, ha='right')

    plt.tight_layout()

    chart_path = "static/charts/chart.png"

    plt.savefig(chart_path)

    plt.close()

    return chart_path