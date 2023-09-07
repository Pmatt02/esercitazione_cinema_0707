from pydantic import BaseModel

class BookingModels (BaseModel):
    
    first_name : str
    last_name : str
    n_tickets : int
    screening_id : int
