import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ParentService {
  private apiUrl = 'http://localhost:5286/api/ParentClass';

  constructor(private http: HttpClient) {}

  // Read
  getConfirmRequest(id: string): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}?UserId=${id}`);
  }

  // Delete
  deleteParent(id: string): Observable<any> {
    return this.http.delete<any>(`${this.apiUrl}/${id}`);
  }

  //Create parent
  createParent(parent: any): Observable<any> {
    return this.http.post<any>(this.apiUrl, parent);
  }

  // Get all parents
  getParents(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl);
  }

  // Get parent by id
  getParent(id: string): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/${id}`);
  }

  // Get parent by name
  getParentsByName(name: string): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/name/${name}`);
  }

  //Update parent
  updateParent(parent: any): Observable<any> {
    return this.http.put<any>(`${this.apiUrl}/${parent.id}`, parent);
  }

  //Create many parents
  addManyParents(parents: any[]): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/many`, parents);
  }
}
