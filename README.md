# 📄 PortfoliAI – Resume & Job Matching Engine

**PortfoliAI** is a lightweight AI-powered tool that semantically matches resumes to job descriptions using OpenAI Embeddings. It helps identify the best candidate–job fit by comparing real content, not just keywords.

This project showcases practical skills in:
- Embedding and comparing text data
- Automating document workflows
- Building MLOps-like data pipelines with NLP

---

## 🔍 What It Does

- Embeds each resume and job description using OpenAI's `text-embedding-ada-002`
- Compares the vectors using cosine similarity
- Ranks job matches for each resume with confidence scores

---

## 🧠 Tech Stack

- Python
- OpenAI API (v1.x)
- PyPDF2
- `scikit-learn` (cosine similarity)
- `dotenv` for key management

---

## 📂 Project Structure
PortfoliAI/
├── main.py # Core script to run the matcher
├── embedder.py # PDF embedding logic
├── matcher.py # Cosine similarity matcher
├── data/
│ ├── resumes/ # Sample resumes (.pdf)
│ └── jobs/ # Sample job descriptions (.pdf)
├── .env.example # Template for secret key
├── requirements.txt
└── README.md

## 🚀 Setup Instrcutions

```bash
# 1. Clone the project
git clone https://github.com/SravyaNMedaramitla/PortfoliAI.git
cd PortfoliAI

# 2. Set up virtual environment
python -m venv .venv
source .venv/Scripts/activate  # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set your OpenAI API key
cp .env.example .env
# then edit .env with your OPENAI_API_KEY

# 5. Run the matcher
python main.py

```
## Sample Output

🔍 Matching resumes to job descriptions...

- ✅ john_smith.pdf → Best Match: jane_doe.pdf (Score: 0.88)
- ✅ lisa_ray.pdf → Best Match: jane_doe.pdf (Score: 0.86)
- ✅ resume_david_mlops.pdf → Best Match: job_mlops_specialist.pdf (Score: 0.86)
- ✅ resume_michael_ai.pdf → Best Match: job_ai_engineer.pdf (Score: 0.85)
- ✅ resume_sophia_frontend.pdf → Best Match: job_frontend_dev.pdf (Score: 0.85)


🧑‍💻 Built By
Sravya Medaramitla
AI Engineer | Full Stack Developer
🔗 LinkedIn - www.linkedin.com/in/sravya-neha