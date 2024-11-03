import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class LoginService {
  private apiUrl = 'http://localhost:5286/api/User';

  constructor(private http: HttpClient) {}

  // login
  login(username: string, password: string): Observable<any> {
    return this.http.get<any>(
      `${this.apiUrl}/login?username=${username}&password=${password}`
    );
  }

  // register
  register(username: string, password: string): Observable<any> {
    return this.http.get<any>(
      `${this.apiUrl}/register?username=${username}&password=${password}`
    );
  }
}
