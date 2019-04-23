import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';


import {MainComponent} from './main/main.component';
import {CreateTasklistComponent} from './create-tasklist/create-tasklist.component';

const routes: Routes = [
  {path: '', redirectTo: '/main', pathMatch: 'full'},
  {path: 'main', component: MainComponent},
  {path: 'createtl', component: CreateTasklistComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
