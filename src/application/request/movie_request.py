from pydantic import BaseModel

class MovieRequest(BaseModel):
    search_text:str