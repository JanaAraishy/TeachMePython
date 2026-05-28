import chromadb
from chromadb.utils import embedding_functions
import pandas as pd

data=pd.read_csv("faq_dataset.csv",encoding="latin-1")

embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)


chroma_client = chromadb.Client(
    chromadb.config.Settings(
        persist_directory="./chroma_db"
    )
)


collection = chroma_client.get_or_create_collection(
    name="profile_collection",
    embedding_function=embedding_function
)

#with open("ai.txt", "r", encoding="utf-8") as file:
    #text = file.read()
text=[
    f"Question: {row['Question']}\nAnswer:{row['Answer']}"
    for _,row in data.iterrows()
]


#chunks = [chunk.strip() for chunk in text.split("\n\n") if chunk.strip()]

#print(f"Loaded {len(text)} chunks from Black hole - Wikipedia.pdf")


for i, row in enumerate(text):
    collection.add(
        documents=[row],
        ids=[f"id_{i}"],
        metadatas=[{"source":"csv"}]
    )

print(f"Stored {len(text)} Q&A pairs")
def get_collection():
    return collection



