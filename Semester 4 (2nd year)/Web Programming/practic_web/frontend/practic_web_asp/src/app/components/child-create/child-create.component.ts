import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { ChildService } from '../../service/child.service';
import { FormsModule } from '@angular/forms';
import { ParentService } from '../../service/parent.service';
import { CommonModule } from '@angular/common';

@Component({
    selector: 'app-child-create',
    templateUrl: './child-create.component.html',
    styleUrls: ['./child-create.component.css'],
    standalone: true,
    imports: [FormsModule, CommonModule]
})
export class ChildCreateComponent {
    child = { name: '', powers: '', age: 0, rank: 0 };

    constructor(private childService: ChildService, private router: Router, private parentService: ParentService) { }

    ngOnInit(): void {
        if (sessionStorage.getItem("userId") == null) {
            this.router.navigate([' ']);
        }
    }

    createChild(): void {
        this.childService.createChild(this.child).subscribe(() => {
            this.router.navigate(['/child-list']);
        });
    }
}