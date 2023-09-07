import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { MoviesComponent } from './movies/movies.component';
import { TicketComponent } from './ticket/ticket.component';
import { FilmDetailsComponent } from './film-details/film-details.component';

const routes: Routes = [

  {path: '', component: HomeComponent},
  {path: 'movies', component: MoviesComponent},
  {path: 'ticket', component: TicketComponent},
  {path: 'filmDetails/:id', component: FilmDetailsComponent},
  {path: 'movies/filmDetails/:id', component: FilmDetailsComponent}

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
