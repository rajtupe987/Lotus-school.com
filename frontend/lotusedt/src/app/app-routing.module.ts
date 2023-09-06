import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { InstructorListComponent } from './componants/instructor-list/instructor-list.component';
import { InstructorLoginComponentComponent } from './componants/instructor-login-component/instructor-login-component.component';
import { HomeComponent } from './componants/home/home.component';
import { AdminComponent } from './componants/admin/admin.component';
import { InstructorPageComponent } from './componants/instructor-page/instructor-page.component';
import { AllcoursesComponent } from './componants/allcourses/allcourses.component';
import { RegisterComponent } from './componants/register/register.component';
import { CreatecourseComponent } from './componants/createcourse/createcourse.component';
import { StudentprofileComponent } from './componants/studentprofile/studentprofile.component';
import { InstructorProfileComponent } from './componants/instructor-profile/instructor-profile.component';
import { AssignmentComponent } from './componants/assignment/assignment.component';

const routes: Routes = [
  {path:'',redirectTo:'/home',pathMatch:'full'},
  {path:'admin-page',redirectTo:'/admin-page',pathMatch:'full'},
  {path:'instructor-page',redirectTo:'/instructor-page',pathMatch:'full'},
  {path:'register-student',redirectTo:'/register-student',pathMatch:'full'},
  {path:'creat-course',redirectTo:'./creat-course'},
  {path:'student-profile',redirectTo:'./student-profile'},
  {path:'register-student',component:RegisterComponent},
  {path:'student-profile',component:StudentprofileComponent},
  

  {path:'Instructor-profile',component:InstructorProfileComponent},
  {path:"Instructor-profile",redirectTo:'./Instructor-profile'},
 
  {path:'create-assignment',component:AssignmentComponent},
  {path:'create-assignment',redirectTo:'./create-assignment'},
 
  {path:'creat-course',component:CreatecourseComponent},
  {path:'all-courses',component:AllcoursesComponent},
  {path:'all-courses',redirectTo:'/all-courses',pathMatch:'full'},
  {path:'home',component:HomeComponent},
  {path:'admin-page',component:AdminComponent},
  {path:'instructor-page',component:InstructorPageComponent},
  { path: 'instructor', redirectTo: '/create-instructor', pathMatch: 'full' },
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
