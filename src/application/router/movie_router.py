from fastapi import APIRouter
from request.movie_request import MovieRequest
from service.movies import search_movies

movie_llm_router = APIRouter()

@movie_llm_router.post("/movies",response_model=str)
def get_movies(movie_request:MovieRequest):
    return search_movies(movie_request.search_text)