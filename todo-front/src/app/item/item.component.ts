import {Component, Input, OnInit} from '@angular/core';
import {ProviderService} from '../shared/services/provider.service';

@Component({
  selector: 'app-item',
  templateUrl: './item.component.html',
  styleUrls: ['./item.component.css']
})
export class ItemComponent implements OnInit {

  @Input() name = 'default name';

  public message = '';

  constructor() { }

  ngOnInit() {
  }

}
