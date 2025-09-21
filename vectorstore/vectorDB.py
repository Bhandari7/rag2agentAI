from langchain_community.vectorstores import FAISS
from langchain_chroma import Chroma


def create_vectorstore(documents, embeddings):
    return FAISS.from_documents(documents, embeddings)

def search_vectorstore(vectorstore, query, k=1):    # add this in input option under fastAPI
    return vectorstore.similarity_search(query, k=k)

def create_vectorstore_chroma(documents, embeddings):
    return Chroma.from_documents(documents, embeddings, persist_directory="./chroma_db")
   
def do_similarity_search(query, embeddings):
    return create_vectorstore_chroma(query, embeddings).similarity_search(query)

def save_vector_db(vectorstore, vector_db_name):    ## add error handling and success messages
    if vector_db_name == 'Chroma':
        print("saving chroma: In latest Chroma, Persistence is done automatically when you create the vectorstore with persist_directory")
    elif vector_db_name == "faiss":
        return vectorstore.save_local("FAISS_Index")
    
def load_vector_db(db_dir_name, vector_db_name, embedding):
    if vector_db_name == 'Chroma':
        print("from loading chroma:::")
        return Chroma(persist_directory=db_dir_name, embedding_function=embedding)
    elif vector_db_name == "faiss":
        return FAISS.load_local(db_dir_name, embedding, allow_dangerous_deserialization=True)
    
