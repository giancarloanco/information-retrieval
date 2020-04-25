import { Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class DocumentsService {

  //name_index = 'text_index';
  name_index = 'test_index';
  address = 'http://127.0.0.1:9200/' + this.name_index;
  address_upload = this.address + '/_doc';
  address_search = this.address + '/_search';

  create_document(title: string, body: string) {
    return this.http.post(this.address_upload, {"title": title, "content": body});
  }

  search_document(input_search: string) {
    return this.http.get(this.address_search + '?q=content:' + input_search)
  }

  search_document_title(input_title_search: string) {
    return this.http.get(this.address_search + '?q=title:' + input_title_search)
  }

  constructor(private http: HttpClient) { }
}
