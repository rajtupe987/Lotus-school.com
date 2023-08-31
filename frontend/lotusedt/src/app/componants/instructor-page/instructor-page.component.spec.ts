import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InstructorPageComponent } from './instructor-page.component';

describe('InstructorPageComponent', () => {
  let component: InstructorPageComponent;
  let fixture: ComponentFixture<InstructorPageComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [InstructorPageComponent]
    });
    fixture = TestBed.createComponent(InstructorPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
