from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
# import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model = "text-embedding-3-large", dimensions=300)

doc = [
    "Virat Kohli is known for his exceptional batting skills, consistency, and aggressive approach to the game.",
    "Rohit Sharma is a talented opening batsman famous for his elegant stroke play and ability to score big hundreds.",
    "Jasprit Bumrah is one of India's leading fast bowlers, recognized for his unique bowling action and deadly yorkers.",
    "Ravindra Jadeja is an excellent all-rounder who contributes with his batting, bowling, and outstanding fielding.",
    "KL Rahul is a versatile batsman who can play effectively across different formats and batting positions."
]
doc_embeddings = embedding.embed_documents(doc)

query = "Tell me about Rohit"
query_embedding = embedding.embed_query(query)

sim_score = cosine_similarity([query_embedding], doc_embeddings)[0]    ##pass both as 2D vectors

index, score = (sorted(list(enumerate(sim_score)), key = lambda x: x[1])[-1])
print(doc[index])
print(f"Similarity score is: {score*100:.2f}%")