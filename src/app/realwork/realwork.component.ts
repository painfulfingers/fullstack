import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';

@Component({
  selector: 'app-realwork',
  templateUrl: './realwork.component.html',
  styleUrl: './realwork.component.css'
})
export class RealworkComponent implements OnInit {
  constructor(private dataservice:DataService){} 
    detector = false 
    new_data:any
    exploded_data:any[] = []
    imploded_data:any[] = []
    

     ngOnInit(): void {
         this.dataservice.gettoken().subscribe((response: any) => {
          this.new_data = response;
             
         });      
     }
     playlist_item(item:string){
      this.dataservice.getitem(item).subscribe((response:any)=>{
       this.exploded_data = response.items;
      });
     }
    item_sorry(item:string){
      console.log(item)
      if (this.imploded_data.length <= 3){
      this.imploded_data.push(item)
      }
    }
    functionality(){
      this.detector = !this.detector;
      if(this.detector == false){
        this.dataservice.getsong(this.imploded_data).subscribe()
      }
      else{
        this.dataservice.pausesong().subscribe()
      }
    }



}    