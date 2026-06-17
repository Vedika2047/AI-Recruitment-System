from parser.resume_service import process_resume
from ai.candidate_summary import generate_summary
from ai.matcher import match_candidate
from analytics.ats_score import calculate_ats_score


def run_recruitment_pipeline(resume_file, job_description):

    try:
        print("Processing resume...")

        candidate = process_resume(resume_file)

        resume_text = str(candidate)

        print("Generating candidate summary...")
        summary = generate_summary(resume_text)

        print("Matching candidate with job description...")
        match_result = match_candidate(
            resume_text,
            job_description
        )

        print("Calculating ATS score...")

        skills = candidate.get("skills", "")
        ats_score = calculate_ats_score(skills)

        return {
            "candidate": candidate,
            "summary": summary,
            "match_result": match_result,
            "ats_score": ats_score
        }

    except Exception as e:
        return {
            "error": str(e)
        }


if __name__ == "__main__":

    print("================================")
    print("     AI Recruitment System")
    print("================================")

    resume_file = input(
        "\nEnter resume file path (.pdf/.docx): "
    )

    job_description = input(
        "\nEnter Job Description:\n"
    )

    result = run_recruitment_pipeline(
        resume_file,
        job_description
    )

    print("\n================================")
    print("            RESULT")
    print("================================")

    if "error" in result:

        print("Error:", result["error"])

    else:

        print("\nCandidate Data:")
        print(result["candidate"])

        print("\nATS Score:")
        print(result["ats_score"])

        print("\nCandidate Summary:")
        print(result["summary"])

        print("\nMatch Result:")
        print(result["match_result"])