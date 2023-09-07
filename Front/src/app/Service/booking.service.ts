import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { I_Booking } from '../Interface/i-Booking';

@Injectable({
  providedIn: 'root'
})
export class BookingService {

  private baseUrl = 'http://localhost:8000';

  constructor(private http: HttpClient) {}

  postBookingData(bookingData: I_Booking): Observable<any> {
    
    console.log(bookingData);
    return this.http.post(this.baseUrl + `/booking/booking`, bookingData)
    
  }

  
}
