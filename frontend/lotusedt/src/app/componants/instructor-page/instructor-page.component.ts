import { Component } from '@angular/core';

@Component({
  selector: 'app-instructor-page',
  templateUrl: './instructor-page.component.html',
  styleUrls: ['./instructor-page.component.css']
})
export class InstructorPageComponent {
  isInstructorLoggedIn: boolean;

  constructor() {
    // Check if Token_of_instructor is present in localStorage
    this.isInstructorLoggedIn = !!localStorage.getItem('Token_of_instructor');
  }
}
