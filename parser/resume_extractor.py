import re

SKILLS_MASTER = [
    "Python",
    "Java",
    "SQL",
    "React",
    "Machine Learning",
    "Data Analysis",
    "NodeJS",
    "C++",
    "HTML",
    "CSS",
    "JavaScript",
    "MySQL",
    "MongoDB",
    "Git",
    "Pandas",
    "Flask",
    "Django"
]


def extract_resume_data(text):

    result = {
        "name": "",
        "email": "",
        "phone": "",
        "skills": "",
        "education": "",
        "experience": ""
    }

    # Extract Name (first non-empty line)
    lines = text.split("\n")

    for line in lines:
        line = line.strip()

        if line:
            result["name"] = line
            break

    # Extract Email
    emails = re.findall(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    if emails:
        result["email"] = emails[0]

    # Extract Phone Number
    phones = re.findall(
        r"\b\d{10}\b",
        text
    )

    if phones:
        result["phone"] = phones[0]

    # Extract Skills
    found_skills = []

    for skill in SKILLS_MASTER:

        if skill.lower() in text.lower():
            found_skills.append(skill)

    result["skills"] = ",".join(found_skills)

    return result