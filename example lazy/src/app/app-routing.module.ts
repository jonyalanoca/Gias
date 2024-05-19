import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PagesModule } from './pages/pages.module';
import { AppComponent } from './app.component';

const routes: Routes = [
  {path:"auth",
    loadChildren:()=> import("./pages/pages.module").then(m=>m.PagesModule)
  },
  {path:"", component:AppComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
