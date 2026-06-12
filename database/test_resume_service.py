from parser.resume_service import process_resume_text

sample_text = """
VEDIKA SATASIYA

Email: vedika2@gmail.com

Phone: 9999999999

Skills:
Python
MySQL
Git
React
"""

candidate = process_resume_text(
    sample_text
)

print(candidate)