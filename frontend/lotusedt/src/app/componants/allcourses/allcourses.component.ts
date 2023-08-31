import { Component,OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-allcourses',
  templateUrl: './allcourses.component.html',
  styleUrls: ['./allcourses.component.css']
})
export class AllcoursesComponent implements OnInit{
  courses: any[] = [];
  currentPage = 1;
  totalPages = 1;

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.fetchCourses(this.currentPage);
  }

  fetchCourses(page: number) {
    this.http.get<any>('http://localhost:8000/all-courses/?page=' + page).subscribe(
      (data) => {
        this.courses = data.results;
        this.currentPage = data.page;
        this.totalPages = data.total_pages;
      },
      (error) => {
        console.error('Error fetching courses:', error);
      }
    );
  }
}
