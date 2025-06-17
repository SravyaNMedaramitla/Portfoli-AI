# matcher.py

import numpy as np


def cosine_similarity(vec1: list, vec2: list) -> float:
    """
    Calculates cosine similarity between two vectors.
    """
    v1 = np.array(vec1)
    v2 = np.array(vec2)

    if np.linalg.norm(v1) == 0 or np.linalg.norm(v2) == 0:
        return 0.0

    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


def find_best_match(resume_vec: list, job_embeddings: dict) -> tuple:
    """
    Given a resume embedding and a dictionary of job embeddings,
    return the best match (job_name, score).
    """
    best_score = -1
    best_job = None

    for job_name, job_vec in job_embeddings.items():
        score = cosine_similarity(resume_vec, job_vec)
        if score > best_score:
            best_score = score
            best_job = job_name

    return best_job, best_score
