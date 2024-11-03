import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
    providedIn: 'root'
})
export class FileService {
    private apiUrl = 'http://localhost/practic_web/users-files/'; // replace with your API endpoint

    constructor(private http: HttpClient) { }

    // List
    getFilesPaginated(pageno: number, id: string): Observable<any[]> {
        return this.http.get<any[]>(this.apiUrl + `GetAllFilesByUser.php?pageno=${pageno}&id=${id}`);
    }

    // login
    login(username: string, password: string): Observable<any> {
        return this.http.post<any>(this.apiUrl + `login.php`, {
            username: username,
            password: password
        });
    }

    // register
    register(username: string, password: string): Observable<any> {
        return this.http.post<any>(this.apiUrl + `register.php`, {
            username: username,
            password: password
        });
    }
}