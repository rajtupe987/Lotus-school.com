import { Component,OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import * as jwt_decode from 'jwt-decode'; // Import the jwt-decode library

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit{
  isAuthenticated: boolean = false;
  userName: string | null = null;
  departments: any[] = [];

  constructor(private http: HttpClient) {}

  toggleCourses(department: any): void {
    department.showCourses = !department.showCourses;
}

  ngOnInit(): void {
    this.fetchDepartments();
    const token=localStorage.getItem('token');
    // Check if user name is present in local storage
    this.userName = localStorage.getItem('userName');
    this.isAuthenticated = !!this.userName;
  }

  fetchDepartments() {
    this.http.get<any[]>('http://localhost:8000/departments-with-courses/').subscribe(
      (data) => {
        this.departments = data;
      },
      (error) => {
        console.error('Error fetching departments:', error);
      }
    );
  }

}



