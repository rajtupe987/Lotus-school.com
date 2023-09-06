import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StudentprofileComponent } from './studentprofile.component';

describe('StudentprofileComponent', () => {
  let component: StudentprofileComponent;
  let fixture: ComponentFixture<StudentprofileComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [StudentprofileComponent]
    });
    fixture = TestBed.createComponent(StudentprofileComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
