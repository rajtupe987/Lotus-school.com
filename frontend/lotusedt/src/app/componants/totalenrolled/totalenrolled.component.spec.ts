import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TotalenrolledComponent } from './totalenrolled.component';

describe('TotalenrolledComponent', () => {
  let component: TotalenrolledComponent;
  let fixture: ComponentFixture<TotalenrolledComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [TotalenrolledComponent]
    });
    fixture = TestBed.createComponent(TotalenrolledComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
