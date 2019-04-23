import { Component, OnInit } from '@angular/core';
import {ProviderService} from '../shared/services/provider.service';

@Component({
  selector: 'app-create-tasklist',
  templateUrl: './create-tasklist.component.html',
  styleUrls: ['./create-tasklist.component.css']
})
export class CreateTasklistComponent implements OnInit {

  constructor(private provider: ProviderService) { }

  public name = '';

  createtasklist() {
    if (this.name !== '') {
      this.provider.create_tasklist(this.name);
    }
  }


  ngOnInit() {
  }

}
