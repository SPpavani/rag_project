import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Path to your PDFs
pdf_path = "data/raw/pdfs/ai_strategy_2024.pdf"

# Load PDF
loader = PyPDFLoader(pdf_path)
docs = loader.load()

# Split into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_documents(docs)

# Save to Chroma DB
persist_dir = "data/vectorstore/chroma_db"
db = Chroma.from_documents(chunks, embeddings, persist_directory=persist_dir)

print(f"✅ Ingestion complete. Database saved at {persist_dir}")
