from pydantic import BaseModel

class ActorModels (BaseModel):

    actor_id: int
    last_name: str
    first_name: str