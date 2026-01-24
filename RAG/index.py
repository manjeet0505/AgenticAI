# filepath: c:\Users\DELL\OneDrive\Desktop\AgenticAI\RAG\index.py
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

pdf_path = Path(__file__).parent / "story.pdf"

loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load()

print(docs[12])