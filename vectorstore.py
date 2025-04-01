import os
import shutil

from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

from config import RAG_FILES_DIR, VECTOR_STORE_PATH


def load_documents():
    docs = []
    processed_dir = os.path.join(RAG_FILES_DIR, 'processed')
    os.makedirs(processed_dir, exist_ok=True)

    files = [
        os.path.join(RAG_FILES_DIR, f)
        for f in os.listdir(RAG_FILES_DIR)
        if f.endswith('.pdf') or f.endswith('.txt')
    ]

    for file in files:
        loader = PyPDFLoader(file) if file.endswith('.pdf') else TextLoader(file)
        docs.extend(loader.load())
        dest_path = os.path.join(processed_dir, os.path.basename(file))
        shutil.move(file, dest_path)

    return docs

def get_vectorstore():
    docs = load_documents()
    if docs:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
        )
        splits = text_splitter.split_documents(docs)
        return Chroma.from_documents(
            documents=splits,
            embedding=OpenAIEmbeddings(),
            persist_directory=VECTOR_STORE_PATH,
        )
    return Chroma(
        embedding_function=OpenAIEmbeddings(),
        persist_directory=VECTOR_STORE_PATH,
    )
