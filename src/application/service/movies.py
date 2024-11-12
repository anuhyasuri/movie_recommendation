from movies_rag.provider import RAGProvider
from movies_rag.prompt.recommender import RecommendationPrompt
import os

def search_movies(query_text):
    provider = RAGProvider(
        index_directory="/Users/anuhyasuri/Documents/gen_ai/Movie_GPT/src/data/vector_store",
        prompt= RecommendationPrompt(details=query_text)
    )
    recommendations = provider.query()
    return str(recommendations)