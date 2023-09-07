import { Component, OnInit } from '@angular/core';
import { I_Film } from '../Interface/i-Films';
import { FilmServiceService } from '../Service/s-film.service';

@Component({
  selector: 'app-movies',
  templateUrl: './movies.component.html',
  styleUrls: ['./movies.component.css']
})
export class MoviesComponent implements OnInit{

  films!: I_Film[];
  paginatedFilms!: I_Film[];
  itemsPerPage = 3;
  currentPage = 1;

  constructor(private film_service: FilmServiceService) {}

  ngOnInit() {
    this.film_service.getAllFilms().subscribe((response: I_Film[]) => {
      this.films = response;
      this.updatePaginatedFilms();
    });
  }

  updatePaginatedFilms() {
    const startIndex = (this.currentPage - 1) * this.itemsPerPage;
    const endIndex = startIndex + this.itemsPerPage;
    this.paginatedFilms = this.films.slice(startIndex, endIndex);
  }

  nextPage() {
    if (this.currentPage < this.totalPages) {
      this.currentPage++;
      this.updatePaginatedFilms();
    }
  }

  prevPage() {
    if (this.currentPage > 1) {
      this.currentPage--;
      this.updatePaginatedFilms();
    }
  }

  get totalPages(): number {
    return Math.ceil(this.films.length / this.itemsPerPage);
  }

}
