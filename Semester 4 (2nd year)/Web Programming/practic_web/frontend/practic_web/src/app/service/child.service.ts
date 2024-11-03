import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ChildService {
  private apiUrl = 'http://localhost/PracticWeb'; // replace with your API endpoint

  constructor(private http: HttpClient) {}

  // List
  getFlights(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl + '/showFlights.php');
  }

  // List by parent id and name
  getFlightsByDateAndDestination(
    date: string,
    destination: string
  ): Observable<any[]> {
    return this.http.get<any[]>(
      `${this.apiUrl}/getFlightsByDateAndDestination.php?date=${date}&destination=${destination}`
    );
  }

  decreaseAvailable(f_id: string, availabe: string): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/decreaseAvailableFlight.php`, {
      f_id: f_id,
      available: availabe,
    });
  }
}
