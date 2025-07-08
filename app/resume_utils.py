# app/resume_utils.py

import PyPDF2
import os

def extract_text_from_pdf(file_path):
    """
    Extract text from a PDF file using PyPDF2.
    Args:
        file_path (str): Relative or absolute path to the PDF file.
    Returns:
        str: Extracted plain text from all pages.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = "\n".join([page.extract_text() or "" for page in reader.pages])
        return text.strip()
