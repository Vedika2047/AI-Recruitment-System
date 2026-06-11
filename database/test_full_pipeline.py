from parser.resume_service import process_resume

candidate = process_resume(
    "resumes/sample_resume.docx"
)

print(candidate)