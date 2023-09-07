import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms'
import { FilmServiceService } from '../Service/s-film.service';
import { I_Film } from '../Interface/i-Films';
import { SScreeningService } from '../Service/s-screening.service';
import { BookingService } from '../Service/booking.service';
import { I_screening } from '../Interface/i-Screening';
import { I_Booking } from '../Interface/i-Booking';
import { HttpHeaders, HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-ticket',
  templateUrl: './ticket.component.html',
  styleUrls: ['./ticket.component.css']
})
export class TicketComponent implements OnInit{

  form: I_Booking = {
    first_name: '',
    last_name: '',
    n_tickets: 0,
    screening_id: 0
  }

  films!: I_Film[];

  selectedFilmId: number | null = null;
  selectedTime: number = -1;
  screening!: I_screening[]

  constructor(
    private film_service: FilmServiceService, 
    private screening_service: SScreeningService, 
    private bookingService: BookingService
  ) {}

  ngOnInit() {
    this.film_service.getAllFilms().subscribe((response: I_Film[]) => {
      this.films = response;
    });
  }

  onFilmSelected() {
    if (this.selectedFilmId) {
      this.screening_service.getScreeningsForFilm(this.selectedFilmId).subscribe(
        (response: I_screening[]) => {
          this.screening = response;
        },
        (error: I_screening) => {
          console.error('Si è verificato un errore nel recupero degli schermi:', error);
        }
      );
    } else {
      this.screening = []; 
    }

    if (this.screening.length > 0) {
      this.form.screening_id = this.screening[0].screening_id;
    } else {
      this.form.screening_id = 0;
    }
  }

  onSubmit(form: NgForm) {

    if (form.valid) {
  
      const bookingData: I_Booking = {
        first_name: this.form.first_name,
        last_name: this.form.last_name,
        n_tickets: this.form.n_tickets,
        screening_id: this.selectedTime
      };  
  
      this.bookingService.postBookingData(bookingData).subscribe(
        (response) => {
          console.log('Prenotazione effettuata:', response);
        },
        (error) => {
          console.error('Errore durante la prenotazione:', error);
        }
      );
    }
  } 

}
