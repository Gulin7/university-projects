import { Component } from '@angular/core';
import { ParentService } from '../../service/parent.service';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
    selector: 'app-parent',
    templateUrl: './parent-create-many.component.html',
    styleUrls: ['./parent-create-many.component.css'],
    standalone: true,
    imports: [FormsModule, CommonModule]
})
export class ParentCreateManyComponent {
    parents: { name: string, userId: string }[] = [];
    parentName = '';
    userId = '';

    ngOnInit(): void {
        if (sessionStorage.getItem("user") == null) {
            this.router.navigate([' ']);
        }
        this.userId = sessionStorage.getItem("user")!;
    }

    constructor(private parentsService: ParentService, private router: Router) { }

    saveParent() {
        this.parents.push({ name: this.parentName, userId: this.userId });
        this.parentName = '';
    }

    submitParents() {
        this.parentsService.addManyParents(this.parents).subscribe(response => {
            console.log(response);
            this.parents = [];
            this.parentName = '';
        });
    }
}