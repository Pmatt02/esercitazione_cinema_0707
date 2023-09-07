from typing import List

from Model.ScreeningModels import ScreeningModels
from DAO.ScreeningDao import ScreeningDao

class ScreeningService:

    def __init__(self, screening_Dao: ScreeningDao):
        self.screening_Dao = screening_Dao

    #screening del film
    def ScreeningFilm(self, film_id: int) -> List[ScreeningModels]:
        return self.screening_Dao.getScreeningByFilmID(film_id)
    
    #film con screening
    def FilmWithScreening(self) -> List[ScreeningModels]:
        return self.screening_Dao.getFilmWithScreening()
    
    #istanza di riferimento come parametro self
    @classmethod
    def service_instance(cls):
        Screening_dao = ScreeningDao()
        return cls(Screening_dao)