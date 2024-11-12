from fastapi import FastAPI
from router.movie_router import movie_llm_router

app = FastAPI()
 
app.include_router(movie_llm_router)

@app.get("/check")
async def root():
    return {"up"}