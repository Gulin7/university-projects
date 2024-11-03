import { Routes } from '@angular/router';
import { ChildCreateComponent } from './components/child-create/child-create.component';
import { ChildListComponent } from './components/child-list/child-list.component';
import { ChildUpdateManyComponent } from './components/child-update-many/child-update-many.component';
import { ChildUpdateComponent } from './components/child-update/child-update.component';
import { ConfirmRequestComponent } from './components/confirm-request/confirm-request.component';
import { LoginComponent } from './components/login/login.component';

export const routes: Routes = [
  { path: '', component: LoginComponent },
  { path: 'childUpdate/:id', component: ChildUpdateComponent },
  { path: 'child-list', component: ChildListComponent },
  { path: 'child-create', component: ChildCreateComponent },
  { path: 'child-update-many', component: ChildUpdateManyComponent },
  { path: 'confirm-request', component: ConfirmRequestComponent },
  { path: '**', redirectTo: '' },
];
