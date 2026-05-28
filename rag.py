from embeddings import get_collection
from langchain_groq import ChatGroq
import os 
from dotenv import load_dotenv

load_dotenv()

collection=get_collection()

llm = ChatGroq(
    model="llama-3.1-8b-instant",           
    api_key=os.getenv("GROQ_API") 
)


def ask_rag(question:str):
    """
    Given a user question:
    1. Query Chroma to find most relevant chunks
    2. Create a context prompt
    3. Ask the LLM to answer based on context
    
    """
       
    results=collection.query(
            query_texts=[question],
            n_results=3
     )
    doc=results["documents"][0]

    context="\n".join(doc)

    prompt = f"""
You are an AI assistant that teaches python. Answer the question based only on the context below.Don't asnswer 
any question that is not related to the context. If you don't know the answer, say you don't know. Do not make up an answer.
try to be helpful and concise. Do not just give short answers, 
try to explain the answer in a way that is easy to understand. Use examples if possible.
Do not mention the context in your answer, just use it to answer the question.
be gentle and encouraging, the user is a beginner in python. 
Always end your answer with a question to keep the conversation going.

Context:
{context}

Question:
{question}

Answer clearly based on the context.
"""
    
    response=llm.invoke(prompt)

    return response.content