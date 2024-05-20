from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate 
from langchain.schema.output_parser import StrOutputParser
# from langchain_core.runnables import RunnablePassthrough # type: ignore

from dotenv import load_dotenv
import os
from colorama import Fore

load_dotenv()

def format_response(result):
    print(Fore.GREEN + result.content + Fore.RESET)

def model_chain(topic):
    model = ChatOpenAI(model = "gpt-3.5-turbo")
    prompt = ChatPromptTemplate.from_template("Tel me a joke about {topic}")

    chain = prompt | model | StrOutputParser()
    return chain.invoke({"topic": input})

# chain.invoke({"topic": "Liverpool FC"})

def main():
    print("===========Menu============")
    print("[1]: If you want a joke")
    print("[2]: If you want to exit")
    print("============================")
    choix = input("Enter your choice: ")

    if choix == "1":
        ask()
    elif choix == "2":
        print("Goodbye!")
        exit()

def ask():
    input_user = input("Give me a topic: ")
    print("Thinking...")
    print(Fore.GREEN + model_chain(input_user) + Fore.RESET)



if __name__ == "__main__":
    main()