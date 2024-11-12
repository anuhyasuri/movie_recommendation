from llama_index.core import (StorageContext, load_index_from_storage)
from typing import List
import tiktoken
from movies_rag.prompts.recommender import RecommendationPrompt
import logging

class RAGProvider:

    def __init__(self, 
                 prompt: RecommendationPrompt, 
                 index_directory: str):
        self.prompt = prompt
        self.index_directory = index_directory

    def query(self) -> str:
        storage_context = StorageContext.from_defaults(persist_dir=self.index_directory)
        index=load_index_from_storage(storage_context=storage_context)
        query_engine=index.as_query_engine()
        formatted_prompt=str(self.prompt)
        logging.info(f"Formatted Prompt: {formatted_prompt}")
        response=query_engine.query(formatted_prompt)
        return response
