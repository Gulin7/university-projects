import { Routes } from '@angular/router';
import { ChildListComponent } from './components/flight-list/child-list.component';
import { ParentListComponent } from './components/hotel-list/parent-list.component';
import { LoginComponent } from './components/login/login.component';
import { PickListComponent } from './pick-list/pick-list.component';

export const routes: Routes = [
  { path: '', component: LoginComponent },
  { path: 'hotel-list', component: ParentListComponent },
  { path: 'flight-list', component: ChildListComponent },
  { path: 'pick-list', component: PickListComponent },
  { path: '**', redirectTo: '' },
];
