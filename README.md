# Retrieval-Augmented Generation (RAG) Project

## 🔍 Overview
This project demonstrates an end-to-end Retrieval-Augmented Generation (RAG) pipeline.  
It combines **document retrieval** with **large language models (LLMs)** to answer questions using both stored knowledge and generative reasoning.  
The goal is to showcase a clean, professional implementation that highlights awareness of modern AI practices.

## 🛠 Tech Stack
- **Python 3.11+**
- **LangChain** – orchestration framework
- **ChromaDB** – local vector database
- **OpenAI API** – LLM for generation
- **fpdf2** – PDF handling (optional for data ingestion)

## 📂 Project Structure
rag_project/
├── README.md
├── requirements.txt
├── src/
│   ├── loaders/        # Data loading scripts (CSV, PDF, APIs)
│   ├── chunkers/       # Text splitting utilities
│   ├── embedders/      # Embedding generation
│   ├── retriever/      # Vector DB retrieval logic
│   ├── generator/      # LLM response generation
│   └── utils/          # Helper functions
├── data/
│   ├── raw/            # Original datasets
│   ├── processed/      # Cleaned & chunked data
│   └── vectorstore/    # Chroma DB files
├── notebooks/          # Experiments & demos
├── configs/            # Config files (API keys, DB settings)
├── scripts/            # Automation scripts
└── tests/              # Unit tests

Code
## 🚀 Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/SPpavani/rag_project.git
   cd rag_project
python -m pip install -r requirements.txt
Install dependencies:
python -m pip install -r requirements.txt
Run the starter script:
python src/main.py


