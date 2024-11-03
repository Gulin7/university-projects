import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class LoginService {
  private apiUrl = 'http://localhost/PracticWeb/'; // replace with your API endpoint

  constructor(private http: HttpClient) {}

  // register
  register(
    username: string,
    date: string,
    destination: string
  ): Observable<any> {
    return this.http.post<any>(this.apiUrl + `register.php`, {
      username: username,
      date: date,
      destination: destination,
    });
  }
}
