from ai.gemini_client import ask_gemini


def generate_summary(resume_text):
    """
    Generate a professional summary from resume text.
    """

    prompt = f"""
    Analyze the following resume.

    Resume:
    {resume_text}

    Return the result in the following format:

    Name:
    Experience:
    Skills:
    Education:
    Strengths:
    Areas for Improvement:
    Overall Recommendation:
    """

    return ask_gemini(prompt)