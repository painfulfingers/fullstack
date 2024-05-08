import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Spotify1Component } from './spotify1.component';

describe('Spotify1Component', () => {
  let component: Spotify1Component;
  let fixture: ComponentFixture<Spotify1Component>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [Spotify1Component]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(Spotify1Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
