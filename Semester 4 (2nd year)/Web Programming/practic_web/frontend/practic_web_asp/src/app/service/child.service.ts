import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ChildService {
  private apiUrl = 'http://localhost:5286/api/ChildClass';

  constructor(private http: HttpClient) {}

  // Create
  createChild(child: any): Observable<any> {
    console.log(child);
    const userId = sessionStorage.getItem('userId');
    return this.http.post<any>(`${this.apiUrl}?userId=${userId}`, child);
  }

  // Read
  getChild(id: string): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/${id}`);
  }

  // List range
  getChildrenRange(start: number, end: number): Observable<any[]> {
    return this.http.get<any[]>(
      `${this.apiUrl}/range?start=${start}&end=${end}`
    );
  }

  getChildren(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl);
  }

  // Update
  updateChild(id: string, child: any): Observable<any> {
    return this.http.put<any>(`${this.apiUrl}/${id}`, child);
  }

  // Update many children
  updateManyChildren(children: any[]): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/many`, children);
  }
}
