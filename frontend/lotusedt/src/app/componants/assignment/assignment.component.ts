import { Component ,OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-assignment',
  templateUrl: './assignment.component.html',
  styleUrls: ['./assignment.component.css']
})
export class AssignmentComponent implements OnInit  {
  courses: any[] = [];
  selectedCourseId: number | null = null;
  assignmentTitle: string = '';
  assignmentDescription: string = '';
  dueDate: string = '';

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    // Fetch courses when the component initializes
    this.http.get<any>('http://localhost:8000/all-courses/').subscribe(response => {
      if (response.results) {
        // Extract the courses array from the response
        this.courses = response.results;
        
        // Optionally, set a default course ID here if needed
        // this.selectedCourseId = this.courses.length > 0 ? this.courses[0].id : null;
      }
    });
  }

  onSubmit(): void {
    if (this.selectedCourseId !== null) {
      // Create an assignment using the selectedCourseId and other form data
      const assignmentData = {
        title: this.assignmentTitle,
        description: this.assignmentDescription,
        course: this.selectedCourseId,
        due_date: this.dueDate // Use "due_date" to match the API's expected field name
      };
  
      // Make an HTTP POST request to create the assignment
      this.http.post('http://localhost:8000/api/assignments/create/', assignmentData).subscribe(
        response => {
          console.log('Assignment created successfully', response);
          // Optionally, reset the form fields here
          this.assignmentTitle = '';
          this.assignmentDescription = '';
          this.selectedCourseId = null; // Reset the selected course
          this.dueDate = '';
        },
        error => {
          console.error('Error creating assignment', error);
        }
      );
    } else {
      console.error('No course selected.'); // Handle this case appropriately
    }
  }
}
