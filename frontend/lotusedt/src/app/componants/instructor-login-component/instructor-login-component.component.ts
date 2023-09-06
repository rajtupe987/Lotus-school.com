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

  constructor(private http: HttpClient) { }

  login() {
    const loginData = {
      email: this.email,
      password: this.password
    };

    // Send the POST request
    this.http.post('http://localhost:8000/verify-intructor', loginData)
      .subscribe(
        (response: any) => {
          // This block is executed if the login is successful
          console.log('Login successful:', response);

          console.log(response)
          // Access the data from the response
          const token = response.token;
          const msg = response.msg;
          const id = response.id;
          const name = response.name;

          alert(response.msg)
          // You can also perform additional actions, such as storing the token in localStorage
          localStorage.setItem("Token_of_instructor", token);
          localStorage.setItem("Instructor_id", id);
          localStorage.setItem("Instructor_name", name);


        },
        (error) => {
          // This block is executed if there's an error during login
          console.error('Login error:', error);
        }
      );
  }

  clear_In_token(): void {
    if (localStorage.getItem("Token_of_instructor")) {
      // Clear the token from local storage or wherever it's stored
      localStorage.removeItem('Token_of_instructor');
      if (localStorage.getItem("Instructor_name")) {
        localStorage.removeItem('Instructor_name')
      }
      if (localStorage.getItem("Instructor_id")) {
        localStorage.removeItem("Instructor_id")// You need to replace 'token' with your actual token key

      }
      alert("You are succseccfully logged out")
    } else {
      alert("You are already logged out")
    }


  }

}
