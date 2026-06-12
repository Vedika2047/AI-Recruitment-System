from ai.matcher import match_candidate

with open("resumes/sample_resume.txt", "r", encoding="utf-8") as file:
    resume_text = file.read()

job_description = """
Looking for a Python Developer.

Requirements:
- Python
- MySQL
- Git
- REST APIs
- Problem Solving

Experience:
1-3 years
"""

result = match_candidate(
    resume_text,
    job_description
)

print("\n===== JOB MATCH RESULT =====\n")
print(result)