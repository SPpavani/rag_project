from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_and_split_pdfs(pdf_paths):
    docs = []
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    for path in pdf_paths:
        loader = PyPDFLoader(path)
        pages = loader.load()
        chunks = splitter.split_documents(pages)
        docs.extend(chunks)
    return docs

if __name__ == "__main__":
    pdf_paths = [
        r"C:\Users\Pavani\rag-project\data\raw\pdfs\employee_handbook.pdf",
        r"C:\Users\Pavani\rag-project\data\raw\pdfs\ai_strategy_2024.pdf"
    ]
    docs = load_and_split_pdfs(pdf_paths)
    print(f"Loaded {len(docs)} chunks")
