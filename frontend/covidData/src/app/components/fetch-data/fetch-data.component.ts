import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { CountryService } from 'src/app/services/country.service';
import { Country } from 'src/app/models/country/country.model';

@Component({
  selector: 'app-fetch-data',
  templateUrl: './fetch-data.component.html',
  styleUrls: ['./fetch-data.component.css']
})
export class FetchDataComponent implements OnInit {

  countries?: Country[];
  code = '';
  message = '';
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
        this.config = {
          id: 'paginate',
          itemsPerPage: 5,
          currentPage: 1,
          totalItems: this.countries.length
        };
      },
      error => {
        console.log(error);
      });
}

  addCountry() {
    this.countryService.getDataRapidAPI(this.code).subscribe(data => {
      this.message = 'The country data was added successfully!';
      this.retrieveCountries();
    },
    error => {
      if(error.error){
        this.message = 'Country Already Exists in the database!';
      } else {
        this.message = 'Error adding country data!';
      }
    });
  }

  view() {
     this.router.navigate(['/country/data/']);
  }

  pageChanged(event : any) {
    this.config.currentPage = event;
  }

}
