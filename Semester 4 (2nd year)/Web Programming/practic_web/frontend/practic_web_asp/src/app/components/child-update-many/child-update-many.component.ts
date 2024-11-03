// child.component.ts
import { Component } from '@angular/core';
import { ChildService } from '../../service/child.service';
import { Router } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ParentService } from '../../service/parent.service';

@Component({
  selector: 'app-child',
  templateUrl: './child-update-many.component.html',
  styleUrls: ['./child-update-many.component.css'],
  standalone: true,
  imports: [CommonModule, FormsModule],
})
export class ChildUpdateManyComponent {
  children: any[] = [];
  updatedChildren: { id: number; name: string; rank: number }[] = [];
  childName = '';

  constructor(
    private childrenService: ChildService,
    private router: Router,
    private parentService: ParentService
  ) {}

  ngOnInit(): void {
    if (sessionStorage.getItem('userId') == null) {
      this.router.navigate([' ']);
    }
    this.childrenService.getChildren().subscribe((children) => {
      this.children = children;
      console.log(children);
    });
  }

  saveChild(id: number, name: string, rank: number) {
    let ok = true;
    this.updatedChildren.forEach((child) => {
      if (child.id == id) {
        ok = false;
      }
    });
    if (ok) {
      this.updatedChildren.push({ id, name, rank });
    }
  }

  submitRequest() {
    this.parentService
      .getConfirmRequest(sessionStorage.getItem('userId')!)
      .subscribe(() => {
        sessionStorage.setItem(
          'updatedChildren',
          JSON.stringify(this.updatedChildren)
        );
        this.router.navigate(['confirm-request']);
      });
  }
}
