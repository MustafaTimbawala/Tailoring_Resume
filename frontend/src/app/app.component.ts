import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { RequestFormComponent } from './request-form/request-form.component';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, RequestFormComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'frontend'; 
  display_text ='';

  updateDisplay(resume: object){ 
    this.display_text = String(resume); 
  }
}
