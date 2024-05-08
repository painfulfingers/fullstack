import { Component,Input,OnInit } from '@angular/core';
import { DataService } from '../data.service';

@Component({
  selector: 'app-working',
  templateUrl: './working.component.html',
  styleUrl: './working.component.css'
})
export class WorkingComponent implements OnInit  {
   constructor(private dataservice:DataService){}

   @Input() data:any

   ngOnInit(): void {
     this.dataservice.posttoken(this.data).subscribe()
     window.location.href =  "http://localhost:4200/realwork"
   }  
}