// spotify.service.ts

import { Injectable } from '@angular/core';
import { ActivatedRoute,Router  } from '@angular/router';
import { BehaviorSubject } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class SpotifyService {
  private tokenSubject = new BehaviorSubject<string | null>(null);
  constructor(
    private route: ActivatedRoute,
    private router: Router
  ) {}

  // Redirect user to Spotify authorization page
  authorize() {
    const redirectUrl = 'http://localhost:4200/callback';
    const scopes = ['playlist-read-collaborative', 'playlist-read-private', 'user-read-private', 'user-read-email', 'playlist-modify-public', 'playlist-modify-private','user-modify-playback-state'];
    const clientId = 'ffdf2044e54040ca9536e13c3f906f73';
    const authorizeUrl = `https://accounts.spotify.com/authorize?client_id=${clientId}&redirect_uri=${encodeURIComponent(redirectUrl)}&scope=${encodeURIComponent(scopes.join(' '))}&response_type=token`;

    window.location.href = authorizeUrl;
  }

  // Handle callback after user authorizes
  handleCallback() {
    this.route.fragment.subscribe((fragment: any) => {
      const token = fragment.split('&')[0].split('=')[1];
      this.tokenSubject.next(token);
    });
  }
  
  getToken() {
    return this.tokenSubject.asObservable(); // Return the BehaviorSubject as an observable
  }
  
  
}