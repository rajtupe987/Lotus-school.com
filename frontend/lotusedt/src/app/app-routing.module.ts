import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { InstructorListComponent } from './componants/instructor-list/instructor-list.component';
import { InstructorLoginComponentComponent } from './componants/instructor-login-component/instructor-login-component.component';




const routes: Routes = [

  { path: '', redirectTo: '/create-instructor', pathMatch: 'full' },
  { path: 'create-instructor', redirectTo: '/create-instructor', pathMatch: 'full' },
  { path: 'verify-instructor', redirectTo: '/verify-instructor', pathMatch: 'full' },
  { path: 'create-instructor', component: InstructorListComponent },
  { path: 'verify-instructor', component: InstructorLoginComponentComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
