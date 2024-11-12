from movies_rag.index import RAGIndexer
import os

def create_index():
    api_key = api_key=os.environ["OPENAI_API_KEY"]
    input_list = ["raw_data/movies.json"]
    provider = RAGIndexer(
        persist_dir= "vector_store/", api_key=api_key)
    provider.create_index(input_list)

create_index()
