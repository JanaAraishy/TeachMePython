# 🐍 Teach Me Python — RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot designed to help users learn Python through context-aware, AI-powered explanations and interactive assistance.

Built using modern AI and backend technologies, this project combines LLMs, vector-based retrieval, and structured backend APIs to deliver accurate and educational responses.

---

## 🚀 Features

- 📚 **Python Learning Assistant** powered by RAG architecture  
- 🤖 Context-aware responses using Groq LLMs  
- 🔍 Document retrieval for accurate, grounded answers  
- ⚡ FastAPI backend for low-latency chatbot interaction  
- 💾 PostgreSQL (Neon) for conversation logging and storage  
- 🖥️ Streamlit UI for interactive chat experience  
- 🧠 Modular architecture for easy scaling and improvements  

---

## 🏗️ Tech Stack

- **Backend:** Python, FastAPI  
- **AI / NLP:** LangChain, Groq
- **Database:** PostgreSQL (Neon)  
- **Frontend:** Streamlit  
- **Architecture:** Retrieval-Augmented Generation (RAG)

---

## 🧠 System Architecture

1. User sends a question via Streamlit UI  
2. FastAPI receives the request  
3. Query is embedded and matched with relevant context (RAG retrieval step)  
4. Relevant documents are passed to Hugging Face LLM  
5. LLM generates a context-aware response  
6. Response is returned to UI and logged in PostgreSQL  

---

