from fastapi import APIRouter, HTTPException
from Model.BookingModels import BookingModels
from Services.Booking_service import BookingService

router = APIRouter(prefix = '/booking', tags = ['Booking'])

@router.post('/booking')
async def booking(booking_data: BookingModels):

    service = BookingService.service_instance()
    result = service.booking(booking_data)

    return result

        