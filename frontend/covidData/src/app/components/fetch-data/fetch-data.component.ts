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
  loading = true;
  message = '';

  constructor(private countryService: CountryService,
    private router: Router) { }

  ngOnInit(): void {
    // this.retrieveCountries();
  }

  retrieveCountries(): void {
    this.countryService.getAll()
    .subscribe(
      data => {
        this.countries= data;
        this.loading = false;
        console.log(data);
      },
      error => {
        console.log(error);
      });
}

  fetch() {
    this.countryService.getDataRapidAPI(this.code).subscribe(data => {
      console.log(data);
      this.message = 'The country data was added successfully!';
    },
    error => {
      console.log(error);
      this.message = 'Error adding country data!';
    })
  }

  view() {
     this.router.navigate(['/country/data']);
  }

}
