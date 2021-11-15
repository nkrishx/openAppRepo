import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { Country } from 'src/app/models/country/country.model';
import { CountryService } from 'src/app/services/country.service';

@Component({
  selector: 'app-countries-list',
  templateUrl: './countries-list.component.html',
  styleUrls: ['./countries-list.component.css']
})
export class CountriesListComponent implements OnInit {

  countries?: Country[];
  currentCountry: Country = {};
  currentIndex = -1;
  code = '';
  selected = false;
  loaded = false;
  config: any;

  constructor(private countryService: CountryService,
    private router: Router) { }

  ngOnInit(): void {
    this.retrieveCountries();
  }

  retrieveCountries(): void {
      this.countryService.getAll()
      .subscribe(
        data => {
          this.countries= data;
          this.loaded = true;
          this.config = {
            id: 'paginate',
            itemsPerPage: 5,
            currentPage: 1,
            totalItems: this.countries.length
          };
        },
        error => {
          this.loaded = true;
          console.log(error);
        });
  }

  refreshList(): void {
    this.retrieveCountries();
    this.currentCountry = {};
    this.currentIndex = -1;
  }

  setActiveCountry(country: Country, index: number): void {
    this.currentCountry = country;
    this.currentIndex = index;
    this.selected = true; 
  }

  pageChanged(event : any) {
    this.config.currentPage = event;
  }

  gotoFetch() {
    this.router.navigate(['country/fetch']);
  }

  // deleteAllCountries(): void {
  //   this.countryService.deleteAll()
  //     .subscribe({
  //       next: (res) => {
  //         console.log(res);
  //         this.refreshList();
  //       },
  //       error: (e) => console.error(e)
  //     });
  // }

  // searchCountryCode(): void {
  //   this.currentCountry = {};
  //   this.currentIndex = -1;

  //   this.countryService.findByCode(this.code)
  //     .subscribe({
  //       next: (data) => {
  //         this.countries = data;
  //         console.log(data);
  //       },
  //       error: (e) => console.error(e)
  //     });
  // }

}
