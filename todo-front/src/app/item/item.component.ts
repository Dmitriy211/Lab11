import {Component, Input, OnInit} from '@angular/core';
import {ProviderService} from '../shared/services/provider.service';
import {ITask} from '../shared/models/task';
import {ITaskList} from '../shared/models/tasklist';


@Component({
  selector: 'app-item',
  templateUrl: './item.component.html',
  styleUrls: ['./item.component.css']
})
export class ItemComponent implements OnInit {

  @Input() name = 'default name';

  public extend = false;

  public tasks: ITask[] = [];

  constructor(private provider: ProviderService) { }

  show_tasks() {
    console.log("hey");
    this.extend = true;

    this.provider.get_tasklist_tasks(this.name).then(res => {
      this.tasks = res;
    });
  }

  ngOnInit() {
  }

}
