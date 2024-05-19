import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { HomeComponent } from './home/home.component';
import { Juego1Component } from './juego1/juego1.component';
import { Juego2Component } from './juego2/juego2.component';

const routes: Routes = [
  {
    path:"",
    children:[
      {path:"home",component:HomeComponent},
      {path:"login",component:LoginComponent},
      {path:"juego1",component:Juego1Component},
      {path:"juego2",component:Juego2Component},
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class PagesRoutingModule { }
