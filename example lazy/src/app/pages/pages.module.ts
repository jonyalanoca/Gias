import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { PagesRoutingModule } from './pages-routing.module';

import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { Juego1Component } from './juego1/juego1.component';
import { Juego2Component } from './juego2/juego2.component';


@NgModule({
  declarations: [
    HomeComponent,
    LoginComponent,
    Juego1Component,
    Juego2Component
  ],
  imports: [
    CommonModule,
    PagesRoutingModule
  ]
})
export class PagesModule { }
