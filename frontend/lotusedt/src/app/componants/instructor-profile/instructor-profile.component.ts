import { Component } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';


@Component({
  selector: 'app-instructor-profile',
  templateUrl: './instructor-profile.component.html',
  styleUrls: ['./instructor-profile.component.css']
})
export class InstructorProfileComponent {
  instructorData: any;

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    // Retrieve the instructor's token from localStorage
    const instructorToken = localStorage.getItem('Token_of_instructor');

    // Make the API call with the authorization header
    if (instructorToken) {
      this.getInstructorProfile(5, instructorToken);
    } else {
      console.error('Instructor token not found in localStorage.');
    }
  }

  getInstructorProfile(instructorId: number, token: string): void {
    const apiUrl = `http://localhost:8000/instructors_profile/${instructorId}`;

    // Set up HTTP headers with the instructor's token for authorization
    const headers = new HttpHeaders({
      'Authorization': `Bearer ${token}`
    });

    // Make the API GET request with the headers
    this.http.get(apiUrl, { headers })
      .subscribe(
        (data: any) => {
          // Handle the API response
          this.instructorData = data;
        },
        (error) => {
          // Handle API error
          console.error('API error:', error);
        }
      );
  }
}
