import { Component, OnInit, Input } from '@angular/core';
import { I_Film } from '../Interface/i-Films';
import { I_screening } from '../Interface/i-Screening';
import { FilmServiceService } from '../Service/s-film.service';
import { SScreeningService } from '../Service/s-screening.service';
import { Subscription, catchError, concat, concatMap, switchMap, tap } from 'rxjs';
import { ActivatedRoute } from '@angular/router';
import { I_Actor } from '../Interface/i-Actor';

@Component({
  selector: 'app-film-details',
  templateUrl: './film-details.component.html',
  styleUrls: ['./film-details.component.css']
})
export class FilmDetailsComponent implements OnInit {

  film!: I_Film;
  screening!: I_screening[];
  private subscription: Subscription | undefined;
  filmActors!: I_Actor[];

  constructor(private filmService: FilmServiceService, private screeningService: SScreeningService, private route: ActivatedRoute) { }

  ngOnInit() {
    this.route.paramMap.pipe(
      concatMap(
        param => this.filmService.filmPlot(param.get("id")!).pipe(
          tap((filmData: I_Film) => {
            this.film = filmData;
            console.log(filmData)
          }),
          catchError((error: any) => {
            console.error('Errore nel caricamento dei dettagli del film:', error);
            return [];
          })
        )
      )
    ).subscribe();

    //screening by id

    this.route.paramMap.pipe(
      concatMap(
        param => this.screeningService.screeningByFilmID(param.get("id")!).pipe(
          tap((screeningData: I_screening[]) => {
            this.screening = screeningData;
            console.log(screeningData);
            
          }),
          catchError((error: any) => {
            console.error('Errore nel caricamento dei dettagli del film:', error);
            return [];
          })
        )
      )
    ).subscribe();

    
    this.route.paramMap.pipe(
      concatMap(
        param => this.filmService.filmActors(param.get("id")!).pipe(
          tap((actorsData: I_Actor[]) => {
            this.filmActors = actorsData;
            console.log(this.filmActors);
          }),
          catchError((error: any) => {
            console.error('Errore nel caricamento degli attori del film:', error);
            return [];
          })
        )
      )
    ).subscribe();

  }

  ngOnDestroy() {
    this.subscription?.unsubscribe();
  }


}
