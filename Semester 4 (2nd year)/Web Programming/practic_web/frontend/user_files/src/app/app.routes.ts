import { Routes } from '@angular/router';
import { FileListComponent } from './components/file-list/file-list.component';
import { LoginComponent } from './components/login/login.component';

export const routes: Routes = [
    { path: 'file-list', component: FileListComponent },
    { path: '', component: LoginComponent }

];
