from langchain_openai import ChatOpenAI, OpenAIEmbeddings

def get_llm():
    return ChatOpenAI(model="gpt-4o")

def get_embeddings():
    return OpenAIEmbeddings()


