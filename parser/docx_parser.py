from docx import Document

def extract_docx_text(file_path):

    try:

        doc = Document(file_path)

        text = ""

        for para in doc.paragraphs:
            text += para.text + "\n"

        return text

    except Exception as e:

        print("DOCX Parsing Error:", e)

        return ""