import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { CountriesListComponent } from './components/countries-list/countries-list.component';
import { CountryDetailsComponent } from './components/country-details/country-details.component';
import { FetchDataComponent } from './components/fetch-data/fetch-data.component';

const routes: Routes = [
  { path: '', redirectTo: 'country/fetch', pathMatch: 'full' },
  { path: 'country/fetch', component: FetchDataComponent },
  { path: 'country/data', component: CountriesListComponent },
  { path: 'country/data/:id', component: CountryDetailsComponent },
  { path: '**', redirectTo: 'country/fetch', pathMatch: 'full' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
