from DAO.utility.db import MySql
from Model.ActorModels import ActorModels

class ActorsDao:

    @classmethod
    def getAllActors(cls):

        MySql.openConnection()
        MySql.query("SELECT * \
                    FROM actor")
        
        data = MySql.getResults()
        
        MySql.closeConnection()
        return data
    
    @classmethod
    def getActorByID(cls, actor_id: int):

        MySql.openConnection()
        MySql.query(f"SELECT * \
                    FROM actor \
                    WHERE actor_id = '{actor_id}'")
        
        data = MySql.getResults()
        
        MySql.closeConnection()
        return data