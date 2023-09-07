from pydantic import BaseModel
from datetime import date

class FilmModels (BaseModel):

    film_id: int
    image: str
    length: int
    plot: str
    rating: float
    title: str
    release_date: date