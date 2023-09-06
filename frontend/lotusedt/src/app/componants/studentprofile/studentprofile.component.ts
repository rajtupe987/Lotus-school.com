import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-studentprofile',
  templateUrl: './studentprofile.component.html',
  styleUrls: ['./studentprofile.component.css']
})
export class StudentprofileComponent {
  studentId!: number | null;
  enrollments: any[] = []; // Initialize enrollments as an empty array

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    // Check if student ID is in localStorage
    const storedStudentId = localStorage.getItem('studentId');

    if (!storedStudentId) {
      // If not found, show an alert and prevent further actions
      alert('Please log in first.');
    } else {
      // If found, set the studentId property
      this.studentId = +storedStudentId; // Parse as number

      // Now you can make an HTTP GET request with the studentId
      this.http.get(`http://localhost:8000/students/${this.studentId}/`)
        .subscribe((data: any) => {
          // Handle the response data as needed
          this.enrollments = data.enrollments; // Assuming the response has an 'enrollments' property
        });
    }
  }
}
