import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
    providedIn: 'root'
})
export class DataService {
    
    private apiUrl = ' http://127.0.0.1:5000/user_playlist';
    private apiUrl2 = ' http://127.0.0.1:5000/user_playlist/api/playlist-items/' 
    private apiurl3 = 'http://127.0.0.1:5000/play'
    private url3 = 'http://127.0.0.1:5000/pause'


    constructor(private http: HttpClient) {}

    posttoken(token:string): Observable<string> {
       const life = this.http.post<string>(this.apiUrl,token);
       return life
    }

    gettoken() : Observable<any[]>{
       const life = this.http.get<any[]>(this.apiUrl)
       return life
   }
    
    getitem(id:string): Observable<string>{
        const life = this.http.get<string>(this.apiUrl2 + id)
        return life 
    }
   
    getsong(ping:any[]): Observable<any[]>{
        const life = this.http.post<any[]>(this.apiurl3 + "/" + ping[0] + "/" + ping[1] + "/" + ping[2],"hello")
        return life
    }
    
    pausesong() : Observable<any>{
        const life = this.http.post<any>(this.url3, "hello")
        return life
    }
}    