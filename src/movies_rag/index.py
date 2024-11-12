from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import (PromptHelper,
                         ServiceContext,
                         SimpleDirectoryReader,
                         VectorStoreIndex)
from llama_index.llms.openai import OpenAI
from typing import List
from llama_index.core.node_parser import SimpleNodeParser
import tiktoken

class RAGIndexer:
    def __init__(self,
                 api_key,
                 persist_dir:str,
                 model:str='gpt-3.5-turbo'):
        self.model=model
        self.persist_dir=persist_dir
        self.llm = OpenAI(
            model=model,
            temperature=0,
            max_tokens=256,
            api_key=api_key
        )
        self.embed_model = OpenAIEmbedding(api_key=api_key)
    
    def create_index(self,
                     input_files:List[str],
                     separator:str=" ",
                     chunk_size:int=1024,
                     chunk_overlap:int=20,
                     prompt_context_window:int=4096,
                     num_output:int=256,
                     chunk_overlap_ratio:float=0.1,
                     chunk_size_limit=None):
        
        node_parser = SimpleNodeParser.from_defaults(
            separator=separator,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            tokenizer=tiktoken.encoding_for_model(self.model).encode #specify the delimiter-tiktoken uses the specified encoding based on the model
        )

        prompt_helper = PromptHelper(
            context_window=prompt_context_window,
            num_output=num_output,
            chunk_overlap_ratio=chunk_overlap_ratio,
            chunk_size_limit=chunk_size_limit
        )

        service_context = ServiceContext.from_defaults(
            llm=self.llm,
            embed_model=self.embed_model,
            node_parser=node_parser,
            prompt_helper=prompt_helper
        )

        documents = SimpleDirectoryReader(input_files=input_files).load_data()

        index = VectorStoreIndex.from_documents(documents, service_context=service_context)
        index.storage_context.persist(persist_dir=self.persist_dir)
