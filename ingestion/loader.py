from langchain_community.document_loaders import (
    WebBaseLoader,
    PyPDFLoader,
    TextLoader
)
from langchain.chains.combine_documents import create_stuff_documents_chain
from pathlib import Path
import os
from transformation.splitter import text_to_create_document



def load_from_web(url: str):
    loader = WebBaseLoader(url)
    return loader.load()


def load_from_pdf(file_path: str):
    if not Path(file_path).exists():
        raise FileNotFoundError(f"PDF file not found: {file_path}")
    loader = PyPDFLoader(file_path)
    return loader.load()


def load_from_text(file_path: str):
    if not Path(file_path).exists():
        raise FileNotFoundError(f"Text file not found: {file_path}")
    loader = TextLoader(file_path, encoding="utf-8")
    return loader.load()


def load_from_source(source_type: str, source: str):
    """
    Unified interface to load documents.
    :param source_type: 'web', 'pdf', or 'text'
    :param source: URL or file path
    :return: List[Document]
    """
    if source_type == "web":
        return load_from_web(source)
    elif source_type == "pdf":
        return load_from_pdf(source)
    elif source_type == "text":
        return load_from_text(source)
    else:
        raise ValueError(f"Unsupported source_type: {source_type}")

def load_multiple_files_from_directory(directory_path, ):       ### refector and use TextLoader for text files
    # loader = create_stuff_documents_chain(llm,prompt)
    documents = []
    directory_path = Path(directory_path)
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if filename.endswith(".txt"):
            with open(file_path, 'r') as f:
                content = f.read()
            documents.extend(text_to_create_document([content]))
        if filename.endswith(".pdf"):
            content = PyPDFLoader(file_path).load()
            documents.extend(content)
    return documents


