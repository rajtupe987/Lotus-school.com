import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-totalenrolled',
  templateUrl: './totalenrolled.component.html',
  styleUrls: ['./totalenrolled.component.css']
})
export class TotalenrolledComponent {
  enrolledStudentsData: any = {}; // Initialize the data variable

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    // Make an HTTP GET request to your Django API
    this.http.get('http://localhost:8000/api/enrolled-students/')
      .subscribe(data => {
        this.enrolledStudentsData = data; // Assign the response data to your variable
      });
  }
}
