from parser.pdf_parser import extract_pdf_text
from parser.docx_parser import extract_docx_text
from parser.resume_extractor import extract_resume_data

from database.candidate_model import insert_candidate


def process_resume_text(text):

    candidate = extract_resume_data(text)

    candidate["education"] = ""
    candidate["experience"] = ""

    try:
        insert_candidate(candidate)
        print("Candidate Inserted Successfully")

    except Exception as e:
        print("Insert Error:", e)

    return candidate


def process_resume(file_path):

    if file_path.endswith(".pdf"):

        text = extract_pdf_text(file_path)

    elif file_path.endswith(".docx"):

        text = extract_docx_text(file_path)

    else:

        raise Exception("Unsupported File Type")

    return process_resume_text(text)