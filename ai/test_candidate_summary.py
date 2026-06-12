from ai.candidate_summary import generate_summary

with open("resumes/sample_resume.txt", "r", encoding="utf-8") as file:
    resume_text = file.read()

summary = generate_summary(resume_text)

print("\n===== AI CANDIDATE SUMMARY =====\n")
print(summary)