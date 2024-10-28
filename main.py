from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

llm = OllamaLLM(model="llama3.1")

def main():
    prompt = input("user: ")
    
    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are an interactive chatbot"),
            ("human", "{prompt}")
        ]
    )

    chain = prompt_template | llm
    response = chain.invoke({"prompt": prompt})
    print(f"bot: {response}")
    
if __name__ == "__main__":
    main()
