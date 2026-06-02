"""
Core RAG Pipeline Module
Combines document retrieval with LLM-based generation
"""

import logging
from typing import List, Dict, Any
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

logger = logging.getLogger(__name__)


class RAGPipeline:
    """Complete RAG (Retrieval-Augmented Generation) Pipeline"""
    
    def __init__(self, 
                 vectorstore_path: str,
                 embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2",
                 llm_model: str = "gpt-3.5-turbo",
                 search_k: int = 3,
                 openai_api_key: str = None):
        """
        Initialize RAG pipeline
        
        Args:
            vectorstore_path: Path to Chroma database
            embedding_model: HuggingFace embedding model name
            llm_model: OpenAI LLM model name
            search_k: Number of documents to retrieve
            openai_api_key: OpenAI API key
        """
        self.vectorstore_path = vectorstore_path
        self.embedding_model_name = embedding_model
        self.llm_model = llm_model
        self.search_k = search_k
        
        self.embeddings = None
        self.vectorstore = None
        self.retriever = None
        self.qa_chain = None
        
        self._initialize(openai_api_key)
    
    def _initialize(self, openai_api_key: str = None):
        """Initialize embeddings, vectorstore, and QA chain"""
        try:
            # Initialize embeddings
            logger.info(f"Loading embeddings: {self.embedding_model_name}")
            self.embeddings = HuggingFaceEmbeddings(
                model_name=self.embedding_model_name
            )
            
            # Load vectorstore
            logger.info(f"Loading vectorstore from: {self.vectorstore_path}")
            self.vectorstore = Chroma(
                persist_directory=self.vectorstore_path,
                embedding_function=self.embeddings
            )
            
            # Create retriever
            self.retriever = self.vectorstore.as_retriever(
                search_kwargs={"k": self.search_k}
            )
            
            # Initialize LLM
            logger.info(f"Initializing LLM: {self.llm_model}")
            llm = ChatOpenAI(
                model_name=self.llm_model,
                api_key=openai_api_key,
                temperature=0.7
            )
            
            # Create QA chain with custom prompt
            prompt_template = """Use the following pieces of context to answer the question at the end. 
If you don't know the answer, just say that you don't know, don't try to make up an answer.

{context}

Question: {question}
Answer:"""
            
            prompt = PromptTemplate(
                template=prompt_template,
                input_variables=["context", "question"]
            )
            
            self.qa_chain = RetrievalQA.from_chain_type(
                llm=llm,
                chain_type="stuff",
                retriever=self.retriever,
                chain_type_kwargs={"prompt": prompt},
                return_source_documents=True
            )
            
            logger.info("✅ RAG Pipeline initialized successfully")
        
        except Exception as e:
            logger.error(f"❌ Error initializing RAG Pipeline: {str(e)}")
            raise
    
    def query(self, question: str) -> Dict[str, Any]:
        """
        Execute RAG query
        
        Args:
            question: User question
            
        Returns:
            Dictionary with answer and source documents
        """
        if not self.qa_chain:
            raise RuntimeError("RAG Pipeline not initialized")
        
        try:
            logger.info(f"Processing query: {question}")
            result = self.qa_chain({"query": question})
            
            return {
                "answer": result["result"],
                "sources": [doc.page_content[:200] for doc in result["source_documents"]],
                "source_count": len(result["source_documents"])
            }
        
        except Exception as e:
            logger.error(f"❌ Error processing query: {str(e)}")
            raise
    
    def retrieve_documents(self, query: str, k: int = None) -> List[Dict]:
        """
        Retrieve relevant documents without generation
        
        Args:
            query: Search query
            k: Number of documents to return
            
        Returns:
            List of relevant documents
        """
        if not self.retriever:
            raise RuntimeError("Retriever not initialized")
        
        k = k or self.search_k
        
        try:
            docs = self.retriever.get_relevant_documents(query)
            return [
                {
                    "content": doc.page_content,
                    "metadata": doc.metadata
                }
                for doc in docs[:k]
            ]
        
        except Exception as e:
            logger.error(f"❌ Error retrieving documents: {str(e)}")
            raise


def setup_logging():
    """Configure logging for RAG pipeline"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
