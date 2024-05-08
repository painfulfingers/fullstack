import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { Spotify1Component } from './spotify1/spotify1.component';
import { RedirectionComponent } from './redirection/redirection.component';
import { RealworkComponent } from './realwork/realwork.component';

const routes: Routes = [{path:'', component:RedirectionComponent},
{path:'callback', component:Spotify1Component},{path:'realwork', component:RealworkComponent}];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
