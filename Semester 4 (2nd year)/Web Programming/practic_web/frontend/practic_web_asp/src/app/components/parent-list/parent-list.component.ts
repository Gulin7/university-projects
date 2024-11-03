import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ParentService } from '../../service/parent.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-parent-list',
  templateUrl: './parent-list.component.html',
  styleUrls: ['./parent-list.component.css'],
  standalone: true,
  imports: [CommonModule],
})
export class ParentListComponent implements OnInit {
  parents: any[] = [];

  constructor(private parentService: ParentService, private router: Router) {}

  ngOnInit(): void {
    if (sessionStorage.getItem('user') == null) {
      this.router.navigate([' ']);
    }
    const result = this.parentService.getParents();
    console.log(result);
    result.subscribe((parents) => {
      console.log(parents);
      this.parents = parents;
    });
  }

  refresh(name: string): void {
    this.parentService.getParentsByName(name).subscribe((parents) => {
      this.parents = parents;
    });
  }

  refreshFrontend(name: string): void {
    this.parentService.getParents().subscribe((parents) => {
      this.parents = parents;
      console.log(this.parents);
      console.log(name);
      if (name) {
        //to contain only the parent that contain the name
        this.parents = this.parents.filter((parent) =>
          parent.name.toLowerCase().includes(name.toLowerCase())
        );
      }
    });
  }

  createParent(): void {
    this.router.navigate(['/parent-create']);
  }

  createParentMany(): void {
    this.router.navigate(['/parent-create-many']);
  }

  updateParent(id: string): void {
    this.router.navigate(['/parent-update', id]);
  }

  deleteParent(id: string): void {
    this.parentService.deleteParent(id).subscribe((thing: any) => {
      console.log(thing);
      // remove the deleted parent from the list
      this.refreshFrontend('');
    });
  }

  logout(): void {
    sessionStorage.clear();
    this.router.navigate([' ']);
  }
}
