import { Component,OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit{
  departments: any[] = [];

  constructor(private http: HttpClient) {}

  toggleCourses(department: any): void {
    department.showCourses = !department.showCourses;
}

  ngOnInit(): void {
    this.fetchDepartments();
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



