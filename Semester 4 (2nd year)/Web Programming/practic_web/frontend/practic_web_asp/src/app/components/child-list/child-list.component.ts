import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { ChildService } from '../../service/child.service';

@Component({
  selector: 'app-child-list',
  templateUrl: './child-list.component.html',
  styleUrls: ['./child-list.component.css'],
  standalone: true,
  imports: [CommonModule, FormsModule],
})
export class ChildListComponent implements OnInit {
  children: any[] = [];
  start: number = 0;
  end: number = 0;

  constructor(private childService: ChildService, private router: Router) {}

  ngOnInit(): void {
    if (sessionStorage.getItem('userId') == null) {
      this.router.navigate([' ']);
    }
    this.childService.getChildren().subscribe((children) => {
      this.children = children;
    });
    this.start = 0;
    this.end = this.children.length;
  }

  filter(): void {
    console.log(this.start, this.end);
    this.childService
      .getChildrenRange(this.start, this.end)
      .subscribe((children) => {
        this.children = children;
      });
  }

  updateChild(id: string): void {
    console.log('updateChild');
    this.router.navigate(['/childUpdate/' + id]);
  }

  createChild(): void {
    this.router.navigate(['/child-create']);
  }

  updateChildMany(): void {
    this.router.navigate(['/child-update-many']);
  }

  logout(): void {
    sessionStorage.removeItem('userId');
    this.router.navigate(['']);
  }
}
