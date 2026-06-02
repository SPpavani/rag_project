import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration management for RAG project"""
    
    # API Keys
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    
    # Paths
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR = os.path.join(PROJECT_ROOT, "data")
    RAW_DATA_DIR = os.path.join(DATA_DIR, "raw")
    PROCESSED_DATA_DIR = os.path.join(DATA_DIR, "processed")
    VECTORSTORE_DIR = os.path.join(DATA_DIR, "vectorstore", "chroma_db")
    PDF_DIR = os.path.join(RAW_DATA_DIR, "pdfs")
    
    # Models
    EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
    LLM_MODEL = "gpt-3.5-turbo"
    
    # RAG Parameters
    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 200
    SEARCH_K = 3
    
    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    
    @classmethod
    def validate(cls):
        """Validate required configuration"""
        if not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY not set. Please configure .env file")
        
        # Create directories if they don't exist
        os.makedirs(cls.PDF_DIR, exist_ok=True)
        os.makedirs(cls.PROCESSED_DATA_DIR, exist_ok=True)
        os.makedirs(os.path.dirname(cls.VECTORSTORE_DIR), exist_ok=True)


if __name__ == "__main__":
    Config.validate()
    print("✅ Configuration validated successfully")
