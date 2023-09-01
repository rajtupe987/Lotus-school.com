import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreatecourseComponent } from './createcourse.component';

describe('CreatecourseComponent', () => {
  let component: CreatecourseComponent;
  let fixture: ComponentFixture<CreatecourseComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CreatecourseComponent]
    });
    fixture = TestBed.createComponent(CreatecourseComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
