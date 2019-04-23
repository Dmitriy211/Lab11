import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { MainComponent } from './main/main.component';
import { AppRoutingModule } from './app-routing.module';
import { ItemComponent } from './item/item.component';

import {ProviderService} from './shared/services/provider.service';
import {HttpClientModule} from '@angular/common/http';
import { CreateTasklistComponent } from './create-tasklist/create-tasklist.component';
import {FormsModule} from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    MainComponent,
    ItemComponent,
    CreateTasklistComponent
  ],
  imports: [
    FormsModule,
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
  ],
  providers: [ProviderService],
  bootstrap: [AppComponent]
})
export class AppModule { }
