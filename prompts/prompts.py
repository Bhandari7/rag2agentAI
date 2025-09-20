from langchain_core.prompts import ChatPromptTemplate

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are an expert AI Engineer. Provide me answers based on the questions"),
        ("user","{input}")
    ]

)
