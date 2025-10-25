import os
import pandas as pd
from pypdf import PdfReader
import docx2txt
from io import BytesIO

def read_pdf(file_path):
    """
    Extracts text from a PDF file.
    """
    try:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text
    except Exception as e:
        return f"Error reading PDF: {e}"

def read_docx(file_path):
    """
    Extracts text from a DOCX file.
    """
    try:
        doc = docx2txt.process(file_path)
        text = ""
        for para in doc.paragraphs:
            text += para.text + "\n"
        return text
    except Exception as e:
        return f"Error reading DOCX: {e}"

def read_data(cvs):
    """
    Reads resumes from a directory and creates a pandas DataFrame.
    """
    data = []

    for file in cvs:
        content = file.read()

        resume_text = ""
        if file.filename.lower().endswith(".pdf"):
            resume_text = read_pdf(BytesIO(content))
        elif file.filename.lower().endswith(".docx"):
            resume_text = read_docx(BytesIO(content))
        # Note: Handling older .doc files requires more complex libraries (e.g., textract)
        # and is not included in this basic example.
        else:
            continue  # Skip files that are not PDF or DOCX

        if resume_text:
            data.append({
                'filename': file.filename,
                'content': resume_text
            })

    return pd.DataFrame(data)