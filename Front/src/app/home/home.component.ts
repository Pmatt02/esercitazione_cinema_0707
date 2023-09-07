import { Component, OnInit } from '@angular/core';
import { FilmServiceService } from '../Service/s-film.service';
import { I_Film } from '../Interface/i-Films';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit{

  films!: I_Film[]

  constructor(private film_service: FilmServiceService) {}

  ngOnInit() {
      
    this.film_service.newlyReleased().subscribe((response: I_Film[]) => {
      this.films = response;
      console.log(this.films)
    });

  }

}
