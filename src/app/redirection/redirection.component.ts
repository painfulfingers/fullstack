import { Component, OnInit } from '@angular/core';
import { SpotifyService } from '../spotify.service';

@Component({
  selector: 'app-redirection',
  templateUrl: './redirection.component.html',
  styleUrl: './redirection.component.css'
})
export class RedirectionComponent implements OnInit {
  constructor(private spotifyservice : SpotifyService){}
  ngOnInit(){
    this.spotifyservice.authorize()
  }        
}
