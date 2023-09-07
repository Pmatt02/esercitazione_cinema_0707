from fastapi import APIRouter, HTTPException

from Services.Film_service import FilmService

router = APIRouter(prefix = '/cinema', tags = ['Film'])


@router.get('/allFilm')
async def all_film():

    service = FilmService.service_instance()
    result = service.allFilm()

    if result == []:

        raise HTTPException(status_code=404, detail="Nessuna film trovato.")

    try:

        return result

    except Exception:

        raise HTTPException(status_code=500, detail="errore")
    
@router.get('/newlyReleased')
async def newly_released():

    service = FilmService.service_instance()
    result = service.newlyReleased()

    if result == []:

        raise HTTPException(status_code=404, detail="Nessuna film rilasciato di recente.")
    
    try:

        return result
    
    except Exception:

        raise HTTPException(status_code=500, detail="errore")

@router.get('/filmPlot/{film_id}')
async def film_plot(film_id: int):

    service = FilmService.service_instance()
    result = service.filmPlot(film_id)

    return result

@router.get('/filmActors/{film_id}')
async def film_actors(film_id: int):

    service = FilmService.service_instance()
    result = service.filmActors(film_id)

    return result