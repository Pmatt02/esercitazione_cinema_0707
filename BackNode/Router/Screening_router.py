from fastapi import APIRouter, HTTPException

from Services.Screening_service import ScreeningService

router = APIRouter(prefix = '/cinema', tags = ['Screening'])

@router.get('/ScreeningByID/{film_id}')
async def film_screening(film_id: int):

    service = ScreeningService.service_instance()
    result = service.ScreeningFilm(film_id)

    return result

@router.get('/FilmWithScreening')
async def film_with_screening():

    service = ScreeningService.service_instance()
    result = service.FilmWithScreening()

    return result