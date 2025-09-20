import os
from dotenv import load_dotenv
load_dotenv(r"C:/Hisalu/.env")
from llm.openai_llm import get_llm, get_embeddings
from ingestion.loader import load_from_web, load_from_pdf, load_from_text
from transformation.splitter import split_documents
from vectorstore.vectorDB import create_vectorstore, search_vectorstore




def main():
    url = "https://docs.smith.langchain.com/administration/concepts#side-effects-of-extended-data-retention-traces-limit"
    query = "What are rate limits in LangSmith? Explain briefly."

    docs = load_from_web(url)
    split_docs = split_documents(docs)
    embeddings = get_embeddings()
    vectorstore = create_vectorstore(split_docs, embeddings)

    results = search_vectorstore(vectorstore, query)
    for i, result in enumerate(results):
        print(f"\n--- Result {i+1} ---\n{result.page_content}\n")


##
if __name__ == "__main__":
    main()
