from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# HuggingFace embeddings wrapper
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Load Chroma DB
persist_dir = "data/vectorstore/chroma_db"
db = Chroma(persist_directory=persist_dir, embedding_function=embeddings)

# Ask a question
query = "What is the AI strategy for 2024?"
results = db.similarity_search(query, k=3)

print("🔎 Query:", query)
for i, doc in enumerate(results, 1):
    print(f"\nResult {i}:")
    print(doc.page_content[:500])
