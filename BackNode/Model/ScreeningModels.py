from pydantic import BaseModel
from datetime import date

class ScreeningModels (BaseModel):

    screening_id: int
    time: date
    film_id: int
    is_bookable: int