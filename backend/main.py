import requests
from bs4 import BeautifulSoup

from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

llm = OllamaLLM(model="llama3.2:1b")


def WebSummarizationAgent(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        result = soup.get_text()
        lines = [l.strip() for l in result.split('\n') if l.strip()]
        text = '\n'.join(lines)
        response = TextSummarizationAgent(text)
        return response
    else:
        return False
    

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