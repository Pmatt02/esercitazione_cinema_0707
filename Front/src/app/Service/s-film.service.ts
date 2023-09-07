import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { I_Film } from '../Interface/i-Films'
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { I_Actor } from '../Interface/i-Actor';


@Injectable({
  providedIn: 'root'
})
export class FilmServiceService {

  base_url: string = 'http://127.0.0.1:8000'

  constructor(private http: HttpClient) {}

  getAllFilms(){
    return this.http.get<I_Film[]>(this.base_url +  '/cinema/allFilm');
  }

  newlyReleased(){
    return this.http.get<I_Film[]>(this.base_url +  '/cinema/newlyReleased');
  }

  filmPlot(film_id: string): Observable<I_Film>{
    return this.http.get<I_Film[]>(this.base_url + `/cinema/filmPlot/${film_id}`).pipe(map(films => films[0]));
  }

  filmActors(film_id: string): Observable<I_Actor[]>{
    return this.http.get<I_Actor[]>(this.base_url +  `/cinema/filmActors/${film_id}`);
  }

}
