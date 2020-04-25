import { Component, OnInit } from '@angular/core';
import { DocumentsService } from "../../services/documents.service";

interface HtmlInputEvent extends Event {
  target: HTMLInputElement & EventTarget;
}

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent implements OnInit {

  num_documents_found: Number;

  title_documents_found = [];
  content_documents_found = [];
  documents_found = [];

  style_results = {display: "none"}

  search_text(input_text: HTMLInputElement): boolean {

    this.document_service.search_document(input_text.value).subscribe(
      res => {
        this.num_documents_found = res["hits"]["hits"].length;

        this.documents_found = [];
        this.title_documents_found = [];
        this.content_documents_found = [];
        
        for (let i=0; i<this.num_documents_found; i++) {
          /*console.log(res["hits"]["hits"][i]);
          this.title_documents_found.push(res["hits"]["hits"][i]["_source"]["title"]);
          this.content_documents_found.push(res["hits"]["hits"][i]["_source"]["content"]);*/
          this.documents_found.push([res["hits"]["hits"][i]["_source"]["title"], res["hits"]["hits"][i]["_source"]["content"]])
        }

        /*console.log(this.title_documents_found);
        console.log(this.content_documents_found);*/
        //console.log(this.documents_found);
        if (this.num_documents_found != 0)
          this.style_results = {display: "unset"}

        },
      err => console.log(err) 
    )
    return false;
  }

  search_text_title(input_text: HTMLInputElement): boolean {

    this.document_service.search_document_title(input_text.value).subscribe(
      res => {
        this.num_documents_found = res["hits"]["hits"].length;

        this.title_documents_found = [];
        this.content_documents_found = [];
        
        for (let i=0; i<this.num_documents_found; i++) {
          /*console.log(res["hits"]["hits"][i]);
          this.title_documents_found.push(res["hits"]["hits"][i]["_source"]["title"]);
          this.content_documents_found.push(res["hits"]["hits"][i]["_source"]["content"]);*/
          this.documents_found.push([res["hits"]["hits"][i]["_source"]["title"], res["hits"]["hits"][i]["_source"]["content"]])
        }

        /*console.log(this.title_documents_found);
        console.log(this.content_documents_found);*/
        console.log(this.documents_found);
        },
      err => console.log(err) 
    )
    return false;
  }

  constructor(private document_service: DocumentsService) { }

  ngOnInit(): void {
  }

}
