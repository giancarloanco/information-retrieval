import { Component, OnInit } from '@angular/core';
import { DocumentsService } from "../../services/documents.service";

interface HtmlInputEvent extends Event {
  target: HTMLInputElement & EventTarget;
}

@Component({
  selector: 'app-index',
  templateUrl: './index.component.html',
  styleUrls: ['./index.component.css']
})
export class IndexComponent implements OnInit {

  upload_new_text(title_input: HTMLInputElement, body_input: HTMLInputElement) {
    console.log("Data")
    console.log(title_input.value)
    console.log(body_input.value)
    this.document_service.create_document(title_input.value, body_input.value).subscribe(
      res => console.log(res),
      err => console.log(err)
    )
  }
  
  constructor(private document_service: DocumentsService) { }

  ngOnInit(): void {
  }

}
