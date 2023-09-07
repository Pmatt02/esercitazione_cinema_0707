import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { I_screening } from '../Interface/i-Screening'; 
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class SScreeningService {

  base_url: string = 'http://127.0.0.1:8000'

  constructor(private http: HttpClient) {}

  screeningByFilmID(film_id: string){
    return this.http.get<I_screening[]>(this.base_url + `/cinema/ScreeningByID/${film_id}`);
  }

  getScreeningsForFilm(filmId: number) {
    return this.http.get<any[]>(this.base_url + `/cinema/ScreeningByID/${filmId}`);
  }
}
