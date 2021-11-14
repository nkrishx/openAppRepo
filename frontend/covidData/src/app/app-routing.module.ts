import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { CountriesListComponent } from './components/countries-list/countries-list.component';
import { CountryDetailsComponent } from './components/country-details/country-details.component';

const routes: Routes = [
  { path: '', redirectTo: 'country/data/', pathMatch: 'full' },
  { path: 'country/data/', component: CountriesListComponent },
  { path: 'country/data/:id', component: CountryDetailsComponent },
  { path: '**', redirectTo: 'country/data/', pathMatch: 'full' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
