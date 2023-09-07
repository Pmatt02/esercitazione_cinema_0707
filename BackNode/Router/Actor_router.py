from fastapi import APIRouter, HTTPException

from Services.Actor_service import ActorService

router = APIRouter(prefix = '/actors', tags = ['Actors'])

@router.get('/allActors')
async def all_actors():

    service = ActorService.service_instance()
    result = service.allActor()

    if result == []:

        raise HTTPException(status_code=404, detail="Nessuna attore trovato.")

    try:

        return result

    except Exception:

        raise HTTPException(status_code=500, detail="errore")
    
@router.get('/ActorByID/{actor_id}')
async def actor_id(actor_id: int):

    service = ActorService.service_instance()
    result = service.actorByID(actor_id)

    if result == []:

        raise HTTPException(status_code=404, detail="Nessuna attore trovato.")

    try:

        return result

    except Exception:

        raise HTTPException(status_code=500, detail="errore")