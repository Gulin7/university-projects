import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ParentService {
  private apiUrl = 'http://localhost/PracticWeb'; // replace with your API endpoint

  constructor(private http: HttpClient) {}

  // Read
  getParent(id: string): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/getHotelById.php?p_id=${id}`);
  }

  // List
  getHotels(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl + '/showHotels.php');
  }

  // List by
  getHotelsByDateAndDestination(
    date: string,
    destination: string
  ): Observable<any[]> {
    return this.http.get<any[]>(
      `${this.apiUrl}/getHotelsByDateAndDestination.php?date=${date}&destination=${destination}`
    );
  }

  //
  decreaseAvailable(h_id: string, available: string): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/decreaseAvailableHotel.php`, {
      h_id: h_id,
      available: available,
    });
  }
}
