import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ReservationService {
  private apiUrl = 'http://localhost/PracticWeb'; // replace with your API endpoint
  constructor(private http: HttpClient) {}

  // Add Reservation
  addReservation(
    username: string,
    date: string,
    type: string,
    type_id: string
  ): Observable<any> {
    console.log(username, date, type, type_id);
    return this.http.post<any>(`${this.apiUrl}/addReservation.php`, {
      username: username,
      date: date,
      type: type,
      type_id: type_id,
    });
  }

  cancelReservation(): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/cancelReservation.php`, {
      username: sessionStorage.getItem('username'),
    });
  }
}
