# TARA — Tool-Augmented Retrieval Assistant

TARA is an AI assistant that combines PDF-based Retrieval-Augmented Generation (RAG) with simple tool selection. It routes user queries to a RAG tool for document-based answers, a calculator for mathematical operations, or a greeting tool for conversational interactions.

## Features
- PDF document loading and text extraction
- Text chunking with RecursiveCharacterTextSplitter
- Sentence Transformer embeddings
- ChromaDB vector storage and retrieval
- Phi-3 Mini language model for answer generation
- Calculator and greeting tools
- Rule-based tool selection

## Repository Contents
This repository contains **both Python (`.py`) files and the Jupyter Notebook (`.ipynb`)** used to build TARA. The Python files are organized in the `src` folder according to the code sequence in the notebook.

## Workflow
PDF → Text Extraction → Chunking → Embeddings → ChromaDB → Tool Selection → RAG / Calculator / Greeting → Answer

## Technologies
Python, PyPDF, LangChain Text Splitters, Sentence Transformers, ChromaDB, FAISS-compatible embeddings, Hugging Face Transformers, Phi-3 Mini, and Google Colab.
