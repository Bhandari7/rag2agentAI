from langchain_community.document_loaders import (
    WebBaseLoader,
    PyPDFLoader,
    TextLoader
)
from pathlib import Path
import os


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
