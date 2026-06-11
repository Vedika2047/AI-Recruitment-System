from analytics.ats_score import (
    calculate_ats_score
)

skills = (
    "Python,MySQL,Git"
)

score = calculate_ats_score(
    skills
)

print(
    "ATS Score:",
    score
)