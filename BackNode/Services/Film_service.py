from typing import List

from Model.FilmModels import FilmModels
from DAO.FilmDao import FilmDao

class FilmService:
    def __init__(self, film_dao: FilmDao) :
        self.film_dao = film_dao

    #all films
    def allFilm(self) -> List[FilmModels]:
        return self.film_dao.getAllFilm()
    
    #newly relased
    def newlyReleased(self) -> List[FilmModels]:
        return self.film_dao.getNewlyReleased()
    
    #film details
    def filmPlot(self, film_id: int) -> List[FilmModels]:
        return self.film_dao.getPlotByFilmID(film_id)
    
    def filmActors(self, film_id: int) -> List[FilmModels]:
        return self.film_dao.getActorsByFilmID(film_id)
    
    #istanza di riferimento come parametro self
    @classmethod
    def service_instance(cls):
        film_dao = FilmDao()
        return cls(film_dao)
    
