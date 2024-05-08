import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RealworkComponent } from './realwork.component';

describe('RealworkComponent', () => {
  let component: RealworkComponent;
  let fixture: ComponentFixture<RealworkComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [RealworkComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(RealworkComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
