import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import {NgxPaginationModule} from 'ngx-pagination';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CountryDetailsComponent } from './components/country-details/country-details.component';
import { CountriesListComponent } from './components/countries-list/countries-list.component';
import { FormsModule } from '@angular/forms';
import { CountryService } from './services/country.service';
import { FetchDataComponent } from './components/fetch-data/fetch-data.component';

@NgModule({
  declarations: [
    AppComponent,
    CountryDetailsComponent,
    CountriesListComponent,
    FetchDataComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    NgxPaginationModule,
    AppRoutingModule,
    FormsModule
  ],
  providers: [CountryService],
  bootstrap: [AppComponent]
})
export class AppModule { }
