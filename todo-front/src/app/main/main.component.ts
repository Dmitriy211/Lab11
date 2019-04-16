import { Component, OnInit } from '@angular/core';
import {ProviderService} from '../shared/services/provider.service';
import {ITaskList} from '../shared/models/tasklist';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  public taskLists: ITaskList[] = [];

  constructor(private provider: ProviderService) { }

  ngOnInit() {
    this.provider.get_tasklists().then(res => {
      this.taskLists = res;
    });
  }

}
