import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("chunks/chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

embeddings = model.encode(chunks)

def retrieve(query):
    query_embedding = model.encode([query])

    similarities = cosine_similarity(query_embedding, embeddings)[0]

    best_index = np.argmax(similarities)

    return chunks[best_index]