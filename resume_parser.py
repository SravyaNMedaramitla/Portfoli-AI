import fitz  # PyMuPDF
import os

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extracts and returns text from a PDF file.
    """
    if not os.path.isfile(pdf_path):
        raise FileNotFoundError(f"File not found: {pdf_path}")

    text = ""
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text()
    except Exception as e:
        raise RuntimeError(f"Failed to parse PDF: {e}")
    
    return text.strip()
