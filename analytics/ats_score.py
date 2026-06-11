REQUIRED_SKILLS = [
    "Python",
    "MySQL",
    "React",
    "Git",
    "Pandas"
]


def calculate_ats_score(candidate_skills):

    if not candidate_skills:
        return 0

    skills = [
        skill.strip()
        for skill in candidate_skills.split(",")
    ]

    score = 0

    points_per_skill = (
        100 / len(REQUIRED_SKILLS)
    )

    for skill in skills:

        if skill in REQUIRED_SKILLS:

            score += points_per_skill

    return int(score)