import os
from embedder import embed_pdf
from matcher import find_best_match

# Define directories
RESUME_DIR = "data/resumes"
JOB_DIR = "data/jobs"


# Validate directories
assert os.path.exists(RESUME_DIR), f"Missing folder: {RESUME_DIR}"
assert os.path.exists(JOB_DIR), f"Missing folder: {JOB_DIR}"

# 1. Embed all resumes
resume_embeddings = {}
for filename in os.listdir(RESUME_DIR):
    if filename.endswith(".pdf"):
        path = os.path.join(RESUME_DIR, filename)
        embedding = embed_pdf(path)
        resume_embeddings[filename] = embedding

# 2. Embed all job descriptions
job_embeddings = {}
for filename in os.listdir(JOB_DIR):
    if filename.endswith(".pdf"):
        path = os.path.join(JOB_DIR, filename)
        embedding = embed_pdf(path)
        job_embeddings[filename] = embedding

# 3. Match each resume to the best job description
print("\n🔍 Matching resumes to job descriptions...\n")

for resume_name, resume_vector in resume_embeddings.items():
    best_job, score = find_best_match(resume_vector, job_embeddings)
    print(f"✅ {resume_name} → Best Match: {best_job} (Score: {score:.2f})")
