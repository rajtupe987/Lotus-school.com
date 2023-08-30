import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule,ReactiveFormsModule  } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { InstructorListComponent } from './componants/instructor-list/instructor-list.component';
import { HttpClientModule } from '@angular/common/http';
import { GetAllExpertiseComponent } from './componants/get-all-expertise/get-all-expertise.component';
import { InstructorLoginComponentComponent } from './componants/instructor-login-component/instructor-login-component.component'; // Import HttpClientModule

@NgModule({
  declarations: [
    AppComponent,
    InstructorListComponent,
    GetAllExpertiseComponent,
    InstructorLoginComponentComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    AppRoutingModule,
    ReactiveFormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
