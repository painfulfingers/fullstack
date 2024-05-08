import { Component,OnInit } from '@angular/core';
import { DataService } from '../data.service';
import { SpotifyService } from '../spotify.service';

@Component({
  selector: 'app-spotify1',
  templateUrl: './spotify1.component.html',
  styleUrl: './spotify1.component.css'
})

export class Spotify1Component implements OnInit{
  data:any;

  constructor(private spotifyservice:SpotifyService){}
   

  ngOnInit(): void {
    this.spotifyservice.handleCallback()
    this.spotifyservice.getToken().subscribe(token => {
      this.data = token;
    })
  }
  
}

