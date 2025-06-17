import os
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

def get_resume_job_match(resume_path, job_path):
    # Load PDFs
    resume_loader = PyPDFLoader(resume_path)
    job_loader = PyPDFLoader(job_path)

    resume_docs = resume_loader.load()
    job_docs = job_loader.load()

    # Combine and split documents
    docs = resume_docs + job_docs
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    split_docs = splitter.split_documents(docs)

    # Embed and store in FAISS
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(split_docs, embeddings)

    retriever = db.as_retriever()
    qa = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(temperature=0),
        chain_type="stuff",
        retriever=retriever
    )

    # Run the QA Chain
    query = "Does this resume match the job description well? Justify your answer and give a percentage score."
    result = qa.run(query)

    return result
