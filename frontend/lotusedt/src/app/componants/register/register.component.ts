import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { ApiService } from 'src/app/expertise.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {

  userData = {
    name: '',
    email: '',
    pass: ''
  };

  logData = {
    email: '',
    pass: ''
  }
  constructor(private authService: ApiService) { }

  signup(): void {
    this.authService.signup(this.userData).subscribe(
      response => {
        this.userData = {
          name: '',
          email: '',
          pass: ''
        }
        console.log(response);
        alert(response.msg) // Handle success
        // Redirect to a success page or perform any necessary actions
      },
      error => {
        console.error(error);
        alert("Error while signup")// Handle error
      }
    );
  }
  login_stduden(): void {

    this.authService.login_stduden(this.logData).subscribe(
      response => {
        this.logData = {
          email: '',
          pass: ''
        }
        console.log(response)
        // Assume you have a JWT token stored in a variable called 'token'
        const token = response.token;

        // Decode the JWT token
        const decodedToken = JSON.parse(atob(token.split('.')[1]));

        // Access user information from the decoded token
        const userId = decodedToken.userId;
        const userName = decodedToken.userName;


        alert(response.msg)
        localStorage.setItem("token", response.token)
        localStorage.setItem("userName", userName)
        localStorage.setItem("studentId", userId)
        // Handle success
      },
      error => {
        console.log(error)
        alert("Error while login")
        // Handle error
      }
    );
  }

  clearToken(): void {
    if (localStorage.getItem("token")) {
      // Clear the token from local storage or wherever it's stored
      localStorage.removeItem('token');
      if (localStorage.getItem("userName")) {
        localStorage.removeItem('userName')
      }
      if (localStorage.getItem("studentId")) {
        localStorage.removeItem("studentId")// You need to replace 'token' with your actual token key

      }
      alert("You are succseccfully logged out")
    } else {
      alert("You are already logged out")
    }


  }
}
