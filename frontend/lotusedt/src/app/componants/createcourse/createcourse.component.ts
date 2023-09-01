import { Component ,OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { ApiService } from 'src/app/expertise.service';

@Component({
  selector: 'app-createcourse',
  templateUrl: './createcourse.component.html',
  styleUrls: ['./createcourse.component.css']
})
export class CreatecourseComponent implements OnInit {
  instructors: any[] = [];
  departments: any[] = [];
  title: string = '';
  description: string = '';

  selectedInstructors: number[] = [];
  selectedDepartment: number | null = null;

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.fetchInstructorsAndDepartments();
  }

  fetchInstructorsAndDepartments(): void {
    this.http.get<any[]>('http://localhost:8000/instructors/').subscribe(
      (instructors) => {
        this.instructors = instructors;
      },
      (error) => {
        console.error('Error fetching instructors', error);
      }
    );

    this.http.get<any[]>('http://localhost:8000/departments-with-courses/').subscribe(
      (departments) => {
        this.departments = departments;
      },
      (error) => {
        console.error('Error fetching departments', error);
      }
    );
  }

  createCourse(): void {
    const courseData = {
      title: this.title,
      description: this.description,
      instructors: this.selectedInstructors,
      department: this.selectedDepartment,
    };

    this.http.post('http://localhost:8000/courses/create/', courseData).subscribe(
      (response) => {
        console.log('Course created successfully', response);
        alert('Course created successfully'); // Show success message to the user
        this.clearForm();
      },
      (error) => {
        console.error('Error creating course', error);
        alert('Error creating course'); // Show error message to the user
      }
    );
  }

  toggleInstructorSelection(instructorId: number) {
    if (this.selectedInstructors.includes(instructorId)) {
      this.selectedInstructors = this.selectedInstructors.filter(id => id !== instructorId);
    } else {
      this.selectedInstructors.push(instructorId);
    }
  }

  clearForm(): void {
    this.title = '';
    this.description = '';
    this.selectedInstructors = [];
    this.selectedDepartment = null;
  }
}
