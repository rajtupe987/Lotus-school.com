import { Component } from '@angular/core';
import { FormBuilder, FormGroup,FormArray, Validators } from '@angular/forms';

import { HttpClient } from '@angular/common/http';

import { ApiService } from 'src/app/expertise.service';
@Component({
  selector: 'app-instructor-list',
  templateUrl: './instructor-list.component.html',
  styleUrls: ['./instructor-list.component.css']
})
export class InstructorListComponent {
  instructorForm!: FormGroup;
  expertiseList: any[] = [];

  constructor(private formBuilder: FormBuilder, private apiService: ApiService) {}

  ngOnInit(): void {
    this.initForm();
    this.getAllExpertise();
  }

  initForm(): void {
    this.instructorForm = this.formBuilder.group({
      first_name: ['', Validators.required],
      last_name: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      password: ['', Validators.required],
      expertise: this.formBuilder.array([], Validators.required)
    });

    // Set initial values to empty strings
    this.instructorForm.setValue({
      first_name: '',
      last_name: '',
      email: '',
      password: '',
      expertise: []
    });
  }

  createInstructor(): void {
    if (this.instructorForm.valid) {
      const instructorData = this.instructorForm.value;
      this.apiService.createInstructor(instructorData).subscribe(
        response => {
          console.log('Instructor created:', response);
          alert("Instructor created")
          this.instructorForm.reset();
        },
        error => {
          console.error('Error creating instructor:', error);
        }
      );
    }
  }

  getAllExpertise(): void {
    this.apiService.getAllExpertise().subscribe(
      response => {
        this.expertiseList = response;
      },
      error => {
        console.error('Error fetching expertise:', error);
      }
    );
  }

  toggleExpertiseSelection(expertiseId: number): void {
    const expertiseArray = this.instructorForm.get('expertise') as FormArray;
    if (expertiseArray.value.includes(expertiseId)) {
      expertiseArray.removeAt(expertiseArray.value.indexOf(expertiseId));
    } else {
      expertiseArray.push(this.formBuilder.control(expertiseId));
    }
  }
}
