from ai.gemini_client import ask_gemini


def match_candidate(resume_text, job_description):
    """
    Compare resume against job description.
    """

    prompt = f"""
    Compare the candidate resume with the job description.

    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Return:

    Match Score (out of 100)

    Matching Skills

    Missing Skills

    Recommendation
    """

    return ask_gemini(prompt)