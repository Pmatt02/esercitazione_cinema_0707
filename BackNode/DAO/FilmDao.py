from DAO.utility.db import MySql

class FilmDao:

    @classmethod
    def getAllFilm(cls):

        MySql.openConnection()
        MySql.query("SELECT * \
                    FROM film")
        
        data = MySql.getResults()

        MySql.closeConnection()
        return data
    
    @classmethod
    def getNewlyReleased(cls):

        MySql.openConnection()
        MySql.query("SELECT film_id, image, title \
                    FROM film \
                    WHERE film.release_date >= DATE_SUB(CURDATE(), INTERVAL 15 DAY);")
        
        data = MySql.getResults()

        MySql.closeConnection()
        return data
    
    @classmethod
    def getPlotByFilmID(cls, film_id: int):

        MySql.openConnection()
        MySql.query(f"SELECT * \
                    FROM film \
                    WHERE film_id = '{film_id}';")

        data = MySql.getResults()

        MySql.closeConnection()
        return data
    
    @classmethod
    def getActorsByFilmID(cls, film_id: int):

        MySql.openConnection()
        MySql.query(f"SELECT a.last_name, a.first_name \
                    FROM actor a \
                    LEFT JOIN film_actor fa ON fa.actor_id = a.actor_id \
                    WHERE fa.film_id = '{film_id}';")

        data = MySql.getResults()

        MySql.closeConnection()
        return data
    
