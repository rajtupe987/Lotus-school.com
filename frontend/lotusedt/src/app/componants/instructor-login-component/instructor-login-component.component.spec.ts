import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InstructorLoginComponentComponent } from './instructor-login-component.component';

describe('InstructorLoginComponentComponent', () => {
  let component: InstructorLoginComponentComponent;
  let fixture: ComponentFixture<InstructorLoginComponentComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [InstructorLoginComponentComponent]
    });
    fixture = TestBed.createComponent(InstructorLoginComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
