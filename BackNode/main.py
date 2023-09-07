from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import Router.Film_router as Film
import Router.Actor_router as Actor
import Router.Booking_router as Booking
import Router.Screening_router as Screening

app = FastAPI()

origins = [
    'http://localhost:4200'
]


app.add_middleware(

    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)

app.include_router(Film.router)
app.include_router(Actor.router)
app.include_router(Booking.router)
app.include_router(Screening.router)
