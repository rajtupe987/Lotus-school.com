import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import jwt_decode from 'jwt-decode';
import { ActivatedRoute } from '@angular/router'; // Add this import
import { formatDate } from '@angular/common'; // Import formatDate for date formatting


@Component({
  selector: 'app-allcourses',
  templateUrl: './allcourses.component.html',
  styleUrls: ['./allcourses.component.css']
})
export class AllcoursesComponent implements OnInit {
  courses: any[] = [];
  currentPage = 1;
  totalPages = 1;

  selectedCourse: any = null; // To store the selected course details


  constructor(
    private http: HttpClient,
    private route: ActivatedRoute // Inject ActivatedRoute
  ) { }

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



  // Function to show course details in the modal box
  showCourseDetails(courseId: number) {
    // Create headers with the authorization token

    const token = localStorage.getItem('token');
    if (!token) {
      alert('Please log in to view course details.');
      return;
    }

    const headers = new HttpHeaders({
      'Authorization': 'Bearer ' + localStorage.getItem('token')
    });

    this.http.get<any>('http://localhost:8000/each_course/' + courseId + '/', { headers }).subscribe(
      (data) => {
        this.selectedCourse = data;
      },
      (error) => {
        console.error('Error fetching course details:', error);
      }
    );
  }



  // Function to close the course details modal box
  closeCourseDetails() {
    this.selectedCourse = null;
  }

  // Function to get instructors as a comma-separated string
  getInstructorsString(instructors: any[]) {
    return instructors.map(instructor => `${instructor.name} (${instructor.expertise.join(', ')})`).join(', ');
  }

  // Property to store enrollment data
  enrollmentData: any = {
    student: null, // Student ID will be set automatically
    course: null,  // Course ID will be set automatically
    enrollment_date: '',
    email: ''
  };


  // Function to enroll in a course
enrollInCourse(courseId: number) {
  console.log('Email value:', this.enrollmentData.email);
  const token = localStorage.getItem('token');
  if (!token) {
    alert('Please log in to enroll in a course.');
    return;
  }

  const headers = new HttpHeaders({
    'Authorization': 'Bearer ' + localStorage.getItem('token')
  });

  // Decode the JWT token to get the student ID
  const decodedToken: any = jwt_decode(token);
  const studentId = decodedToken.userId; // Assuming userId is the student ID in the token payload

  // Set the course ID and student ID in the enrollment data
  this.enrollmentData.course = courseId;
  this.enrollmentData.student = studentId;

  // Format the enrollment date as "YYYY-MM-DD"
  this.enrollmentData.enrollment_date = formatDate(new Date(), 'yyyy-MM-dd', 'en-US');

  this.enrollmentData.email = 'test@example.com';  // Set a default email for testing
  console.log('Email value:', this.enrollmentData.email);
  

  this.http.post('http://localhost:8000/enroll/', this.enrollmentData, { headers }).subscribe(
    (response) => {
      alert('Enrollment successful.');
      this.closeCourseDetails();
    },
    (errorResponse) => {
      if (errorResponse.error && errorResponse.error.message) {
        alert(errorResponse.error.message);
      } else {
        console.error('Error enrolling in the course:', errorResponse);
        alert('Enrollment failed. Please try again later.');
      }
    }
  );
  
  
}

onEmailInput(event: any) {
  const inputValue = event.target.value;
  console.log('Email input value:', inputValue);
}



}
