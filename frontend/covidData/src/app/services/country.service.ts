import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Country } from '../models/country/country.model';

const baseUrl = 'http://localhost:8000/api/v1/country/data'; //base url to fetch data from the populated db
const fetchUrl = 'http://localhost:8000/api/v1/country/fetch'; //base url used for any rapid api related operations including db population

@Injectable({
  providedIn: 'root'
})
export class CountryService {

  constructor(private http: HttpClient) { }

  getAll(): Observable<Country[]> {
    return this.http.get<Country[]>(baseUrl);
  }

  get(id: any): Observable<Country> {
    return this.http.get(`${baseUrl}/${id}/`);
  }

  update(id: any, data: any): Observable<any> {
    return this.http.put(`${baseUrl}/${id}/`, data);
  }

  delete(id: any): Observable<any> {
    return this.http.delete(`${baseUrl}/${id}/`);
  }

  getDataRapidAPI(code: any) {
    // console.log(`${baseUrl}/fetch/`);
    return this.http.get<Country[]>(`${fetchUrl}?code=${code}`);
  }

  // deleteAll(): Observable<any> {
  //   return this.http.delete(baseUrl);
  // }

  // findByCode(countryCode: any): Observable<Country[]> {
  //   return this.http.get<Country[]>(`${baseUrl}?code=${countryCode}`);
  // }


}
