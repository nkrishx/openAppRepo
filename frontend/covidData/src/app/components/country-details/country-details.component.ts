import { Component, OnInit } from '@angular/core';
import { CountryService } from 'src/app/services/country.service';
import { ActivatedRoute, Router } from '@angular/router';
import { Country } from 'src/app/models/country/country.model';

@Component({
  selector: 'app-country-details',
  templateUrl: './country-details.component.html',
  styleUrls: ['./country-details.component.css']
})
export class CountryDetailsComponent implements OnInit {

  currentCountry: Country = {
    country: '',
    code: '',
    confirmed: 0,
    recovered: 0,
    critical: 0,
    deaths: 0,
    latitude: 0,
    longitude: 0
  };
  message = '';
  error = false;

  constructor(
    private countryService: CountryService,
    private route: ActivatedRoute,
    private router: Router
  ) { }

  ngOnInit(): void {
    this.message = '';
    this.getCountry(this.route.snapshot.paramMap.get('id'));
  }

  getCountry(id : any) {
    this.countryService.get(id)
      .subscribe(
        data => {
          this.currentCountry= data;
          console.log(data);
        },
        error => {
          this.error = true;
          console.log(error);
        });
  }

  updateCountry() {
    this.countryService.update(this.currentCountry.id, this.currentCountry)
      .subscribe(
        response => {
          console.log(response);
          this.message = 'The country data was updated successfully!';
        },
        error => {
          console.log(error.message);
          this.message = error.message;
        });
  }

  deleteCountry() {
    this.countryService.delete(this.currentCountry.id)
      .subscribe(
        response => {
          console.log(response);
          this.router.navigate(['/country/data']);
        },
        error => {
          console.log(error);
          this.message = error.message;
        });
  }

  cancel() {
    this.router.navigate(['/country/data']);
  }

}
