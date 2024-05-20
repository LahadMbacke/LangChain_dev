from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate 
from langchain.output_parsers import StrOutputParser 
# from langchain_core.runnables import RunnablePassthrough # type: ignore

from dotenv import load_dotenv
import os
from colorama import Fore

load_dotenv()

def format_response(result):
    print(Fore.GREEN + result.content + Fore.RESET)

model = ChatOpenAI(model = "gpt-3.5-turbo")
prompt = ChatPromptTemplate.from_template("Tel me a joke about {topic}")

chain = prompt | model | format_response

chain.invoke({"topic": "Liverpool FC"})

