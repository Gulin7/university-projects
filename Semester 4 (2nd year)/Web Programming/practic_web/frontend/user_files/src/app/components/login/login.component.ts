
import { Component, NgModule, OnInit } from '@angular/core';
import { Router } from "@angular/router";
import { FileService } from '../../service/file.service';

@Component({
    selector: 'app-login',
    templateUrl: './login.component.html',
    standalone: true,
    styleUrls: ['./login.component.css'],
})
export class LoginComponent implements OnInit {

    constructor(private service: FileService, private router: Router) { }

    ngOnInit(): void {
    }

    login(username: string, password: string) {
        this.service.login(username, password).subscribe((thing: null) => {
            if (thing != null) {
                sessionStorage.setItem("user", thing["id"])
                this.router.navigate(['file-list']).then(_ => { });
            } else alert("Wrong username or password!")
        });
    }

    register(username: string, password: string) {
        this.service.register(username, password).subscribe((thing: null) => {
            if (thing != null) {
                sessionStorage.setItem("user", thing["id"])
                this.router.navigate(['file-list']).then(_ => { });
            } else alert("Username already exists!")
        });
    }

}
