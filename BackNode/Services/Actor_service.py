from typing import List

from Model.ActorModels import ActorModels
from DAO.ActorsDao import ActorsDao

class ActorService:
    def __init__(self, actor_dao: ActorsDao):
        self.actor_dao = actor_dao

    #all actor
    def allActor(self) -> List[ActorModels]:
        return self.actor_dao.getAllActors()
    
    #actor by id
    def actorByID(self, actor_id: int) -> List[ActorModels]:
        return self.actor_dao.getActorByID(actor_id)
    
    @classmethod
    def service_instance(cls):
        actor_dao = ActorsDao()
        return cls(actor_dao)