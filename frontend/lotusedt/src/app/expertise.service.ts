// api.service.ts

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { InstructorData } from './instructor.model'; // Import the interface

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private baseUrl = 'http://localhost:8000/';

  constructor(private http: HttpClient) {}

  createInstructor(data: InstructorData): Observable<any> {
    return this.http.post(`${this.baseUrl}create-instructor`, data);
  }

  getAllExpertise(): Observable<any> {
    return this.http.get(`${this.baseUrl}get-all-expertise/`);
  }

  login(credentials: { email: string; password: string }): Observable<any> {
    return this.http.post(`${this.baseUrl}verify-instructor`, credentials);
  }

  signup(userData: any): Observable<any> {
    const url = `${this.baseUrl}register`;
    return this.http.post(url, userData);
  }

  login_stduden(credentials: any): Observable<any> {
    const url = `${this.baseUrl}login`;
    return this.http.post(url, credentials);
  }
}
