from langchain_community.vectorstores import FAISS

def create_vectorstore(documents, embeddings):
    return FAISS.from_documents(documents, embeddings)

def search_vectorstore(vectorstore, query, k=4):
    return vectorstore.similarity_search(query, k=k)


