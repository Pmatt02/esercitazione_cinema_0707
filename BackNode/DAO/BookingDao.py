from DAO.utility.db import MySql
from Model.BookingModels import BookingModels

class BookingDao:

    @classmethod
    def postBooking(cls, booking_data: BookingModels):

        # if not cls.checkScreeningId(booking_data.screening_id):
        #     raise ValueError("Invalid screening_id")
        
        MySql.openConnection()
        MySql.query(
                    f"INSERT INTO booking(first_name, last_name, n_tickets, screening_id)  \
                    VALUES ('{booking_data.first_name}', '{booking_data.last_name}', '{booking_data.n_tickets}', '{booking_data.screening_id}')"
        )
        MySql.commit()
        MySql.closeConnection()
        #return data