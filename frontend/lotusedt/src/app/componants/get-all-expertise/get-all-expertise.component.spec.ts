import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GetAllExpertiseComponent } from './get-all-expertise.component';

describe('GetAllExpertiseComponent', () => {
  let component: GetAllExpertiseComponent;
  let fixture: ComponentFixture<GetAllExpertiseComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [GetAllExpertiseComponent]
    });
    fixture = TestBed.createComponent(GetAllExpertiseComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
