import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService { 

  baseUrl: string = "http://0.0.0.0:8000 "

  constructor(private http: HttpClient) { }  
  
  // send the form information 
  createResume(userData: any): Observable<any> { 
    return this.http.post(`${this.baseUrl}/create_resume`, userData);
  }

  // get past resumes created  
  getPastResume(): Observable<any> {
  return this.http.get(`${this.baseUrl}/past_resume`);
  }

  // add information to a section for resume  
  modifyResume(resume_data: any, section: any): Observable<any> {  
    const userData: any = { section, resume_data}
    return this.http.post(`${this.baseUrl}/create_resume`, userData);
  } 

}
