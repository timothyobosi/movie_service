from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

fake_movie_db = [
     {  'name':'Star Wars: Episode IX - The Rise of Skywalker',
        'plot':'The surviving members of the resistance face the first Order once again',
        'genres':['Action','Adventure','Fantasy'],
        'casts':['Daisy','Adam Driver']
     }
]

class Movie(BaseModel):
    name: str
    plot: str
    genres: List[str]
    casts: List[str]

@app.get('/', response_model=List[Movie])
async def index():
   return fake_movie_db


