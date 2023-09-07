from DAO.utility.db import MySql

class ScreeningDao:

    @classmethod
    def getScreeningByFilmID(cls, film_id: int):

        MySql.openConnection()
        MySql.query(f"SELECT s.screening_id, s.time, s.film_id, s.is_bookable \
                    FROM screening s \
                    INNER JOIN film f on s.film_id = f.film_id \
                    where f.film_id = '{film_id}';")
        
        data = MySql.getResults()

        MySql.closeConnection()
        return data
    
    @classmethod
    def getFilmWithScreening(cls):

        MySql.openConnection()
        MySql.query("SELECT f.film_id, f.title \
                    FROM film AS f \
                    WHERE EXISTS ( \
                    SELECT 1 \
                    FROM screening AS s \
                    WHERE s.film_id = f.film_id")
        
        data = MySql.getResults()

        MySql.closeConnection()
        return data