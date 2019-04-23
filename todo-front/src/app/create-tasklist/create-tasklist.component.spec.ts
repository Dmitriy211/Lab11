import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateTasklistComponent } from './create-tasklist.component';

describe('CreateTasklistComponent', () => {
  let component: CreateTasklistComponent;
  let fixture: ComponentFixture<CreateTasklistComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CreateTasklistComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CreateTasklistComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
