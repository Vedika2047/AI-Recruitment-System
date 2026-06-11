from parser.resume_extractor import extract_resume_data

sample_text = """
VEDIKA SATASIYA

Email: vedika@gmail.com

Phone: 9876543210

Skills:
Python
MySQL
Pandas
Git
React
"""

data = extract_resume_data(
    sample_text
)

print(data)