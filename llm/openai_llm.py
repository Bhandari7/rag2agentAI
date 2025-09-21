from langchain_openai import ChatOpenAI, OpenAIEmbeddings

def get_llm():
    return ChatOpenAI(model="gpt-4o")
    # return ChatOpenAI(model="gpt-4o-mini")

def get_embeddings():
    # return OpenAIEmbeddings()   # model='text-embedding-ada-002'
    return OpenAIEmbeddings(model="text-embedding-3-large") 

def embedded_query(text, model="text-embedding-3-large"):
    return OpenAIEmbeddings().embed_query(text)