import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain.text_splitter import (CharacterTextSplitter,) 
from langchain.prompts.chat import (HumanMessagePromptTemplate, SystemMessagePromptTemplate)

from langchain.schema import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain.vectorstores import Chroma

from colorama import Fore

load_dotenv()   


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LANGUAGE_MODEL = "gpt-3.5-turbo"

template:str = """/
Vous êtes un spécialiste du support client. Vous assistez les utilisateurs avec des demandes générales basées sur {context} et des problèmes techniques. /
Si vous ne connaissez pas la réponse, vous invitez l'utilisateur à joindre le service support au téléphone ou par mail 
"""
system_messages_prompt = SystemMessagePromptTemplate.from_template(template) # permet de définir le template pour les messages du système
human_messages_prompt = HumanMessagePromptTemplate.from_template(
    input_variable=["question", "context"], 
    template = "{question}"
) # permet de définir le template pour les messages de l'utilisateur

def load_file():
    loader = TextLoader("./docs/faq_fr.txt")
    text_spliter = CharacterTextSplitter(chunk_size=100,chunk_overlap=0) # permet de découper le texte en morceaux de 1000 caractères
    documents = loader.load()
    chunks = text_spliter.split_documents(documents)
    # print(f"Number of documents {len(documents)},Number of chunks: {len(chunks)}")
    return chunks


def load_embeddings(doucuments,user_query):
    db = Chroma.from_documents(doucuments,OpenAIEmbeddings()) # permet de charger les embeddings des documents 
    docs = db.similarity_search(user_query) # permet de chercher les documents les plus similaires à la requête de l'utilisateur
    print(f"Similarity search result: {docs}")
    return db.as_retriever()

def query(query):
   documents =  load_file()
   retriver = load_embeddings(documents,query) # permet de charger les embeddings des documents et de chercher les documents les plus similaires à la requête de l'utilisateur
   
query("Quelle est la capital du Senegal ?")
# query("Quelle est la politique de remboursement ?")