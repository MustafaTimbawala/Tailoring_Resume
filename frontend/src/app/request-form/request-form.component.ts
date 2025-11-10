import { Component, EventEmitter, Output } from '@angular/core'; 
import { ApiService } from '../services/api.service';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-request-form', 
  standalone: true,
  imports: [FormsModule],
  templateUrl: './request-form.component.html',
  styleUrl: './request-form.component.css'
})
export class RequestFormComponent { 
  job_title: string = ""; 
  company_name: string = ""; 
  job_desc: string = "";  

  @Output() newResumeEvent = new EventEmitter<object>();

  constructor(private apiService: ApiService){}
  
  submitForm(){ 
    console.log("The job title is", this.job_title) 

    const userData: any = { 
      "job_title" : this.job_title, 
      "company_title" : this.company_name, 
      "job_description": this.job_desc,
    }
 
    this.apiService.createResume(userData).subscribe({ 
      next: (Response)=>{ 
        console.log("The created Resume is", Response);
        this.newResumeEvent.emit(Response);
      }, 
      error: (error)=> {
        console.error(error); 

      }
    })


  }


}
