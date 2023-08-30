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
}
