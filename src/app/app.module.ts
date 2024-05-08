import { NgModule } from '@angular/core';
import { BrowserModule, provideClientHydration } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { Spotify1Component } from './spotify1/spotify1.component';
import { RedirectionComponent } from './redirection/redirection.component';
import { WorkingComponent } from './working/working.component';
import { RealworkComponent } from './realwork/realwork.component';

@NgModule({
  declarations: [
    AppComponent,
    Spotify1Component,
    RedirectionComponent,
    WorkingComponent,
    RealworkComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [
    provideClientHydration()
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
