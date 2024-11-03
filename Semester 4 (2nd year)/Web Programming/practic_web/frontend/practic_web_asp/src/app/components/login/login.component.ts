
import { Component, NgModule, OnInit } from '@angular/core';
import { Router } from "@angular/router";
import { LoginService } from '../../service/login.service';

@Component({
    selector: 'app-login',
    templateUrl: './login.component.html',
    standalone: true,
    styleUrls: ['./login.component.css'],
})
export class LoginComponent implements OnInit {

    constructor(private service: LoginService, private router: Router) { }

    ngOnInit(): void {
    }

    login(username: string, password: string) {
        this.service.login(username, password).subscribe((thing: null) => {
            console.log(thing)
            if (thing != null) {
                sessionStorage.setItem("userId", thing["id"])
                this.router.navigate(['child-list']).then(_ => { });
            } else alert("Wrong username or password!")
        });
    }

    register(username: string, password: string) {
        this.service.register(username, password).subscribe((thing: null) => {
            console.log(thing)
            if (thing != null) {
                sessionStorage.setItem("userId", thing["id"])
                this.router.navigate(['child-list']).then(_ => { });
            } else alert("Username already exists!")
        });
    }

}
