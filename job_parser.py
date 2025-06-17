import os

def load_job_description(file_path: str) -> str:
    """
    Loads and cleans a job description from a .txt file.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Job file not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    return clean_text(content)


def clean_text(text: str) -> str:
    """
    Basic cleanup for job/resume text (can be extended later).
    """
    lines = text.splitlines()
    lines = [line.strip() for line in lines if line.strip()]
    return " ".join(lines)
