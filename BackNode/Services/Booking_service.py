from typing import List

from Model.BookingModels import BookingModels
from DAO.BookingDao import BookingDao

class BookingService: 
    def __init__(self, booking_dao: BookingDao):
        self.booking_dao = booking_dao

    #post booking
    def booking(self, booking_data: BookingModels) -> List[BookingModels]:
        return self.booking_dao.postBooking(booking_data)
    
    @classmethod
    def service_instance(cls):
        booking_dao = BookingDao()
        return cls(booking_dao)