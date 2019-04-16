import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  taskLists = ['task one', 'task two', 'task three', 'task four', 'task five'];

  constructor() { }

  ngOnInit() {
  }

}
