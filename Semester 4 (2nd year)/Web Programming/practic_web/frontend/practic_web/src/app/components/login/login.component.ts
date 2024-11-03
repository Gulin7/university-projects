import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { LoginService } from '../../service/login.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  standalone: true,
  styleUrls: ['./login.component.css'],
})
export class LoginComponent implements OnInit {
  constructor(private service: LoginService, private router: Router) {}

  ngOnInit(): void {}

  register(username: string, date: string, destination: string) {
    this.service
      .register(username, date, destination)
      .subscribe((thing: null) => {
        console.log(thing);
        if (thing == null) {
          return;
        }
        sessionStorage.setItem('user', thing['id']);
        sessionStorage.setItem('username', thing['username']);
        sessionStorage.setItem('date', date);
        sessionStorage.setItem('destination', destination);
        this.router.navigate(['pick-list']).then((_) => {});
      });
  }
}
