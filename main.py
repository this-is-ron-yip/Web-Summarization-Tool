from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

llm = OllamaLLM(model="llama3.1")


def TextSummarizationAgent(text):    
    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a Text Summarization Agent. Your reponsibility is to generate a concise summary of the provided text"),
            ("human", "{text}")
        ]
    )
    chain = prompt_template | llm
    response = chain.invoke({"text": text})
    return response