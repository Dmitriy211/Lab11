import {EventEmitter, Injectable} from '@angular/core';
import {MainService} from './main.service';
import {HttpClient} from '@angular/common/http';
import {ITaskList} from '../models/tasklist';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {

  public sendMessage = new EventEmitter<string>();

  constructor(http: HttpClient) {
    super(http);
  }

  get_tasklists(): Promise<ITaskList[]> {
    return this.get('http://localhost:8000/tasklists/', {});
  }

  create_tasklist(name: any): Promise<ITaskList> {
    return this.post('http://localhost:8000/tasklists/', {
      name: name
    });
  }
}
