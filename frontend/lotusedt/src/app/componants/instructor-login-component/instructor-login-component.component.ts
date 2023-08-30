import { Component } from '@angular/core';

import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-instructor-login-component',
  templateUrl: './instructor-login-component.component.html',
  styleUrls: ['./instructor-login-component.component.css']
})
export class InstructorLoginComponentComponent {
  email: string = '';
  password: string = '';

  constructor(private http: HttpClient) {}

  login() {
    const loginData = {
      email: this.email,
      password: this.password
    };

    // Send the POST request
    this.http.post('http://localhost:8000/verify-intructor', loginData)
      .subscribe(
        (response) => {
          // This block is executed if the login is successful
          console.log('Login successful:', response);
        },
        (error) => {
          // This block is executed if there's an error during login
          console.error('Login error:', error);
        }
      );
  }
}
