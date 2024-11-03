// child.component.ts
import { Component } from '@angular/core';
import { ChildService } from '../../service/child.service';
import { Router } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ParentService } from '../../service/parent.service';

@Component({
    selector: 'app-child',
    templateUrl: './confirm-request.component.html',
    standalone: true,
    imports: [CommonModule, FormsModule]
})
export class ConfirmRequestComponent {
    updatedChildren: { id: number, name: string; powers: string; age: number; rank: number; }[] = [];

    constructor(private childrenService: ChildService, private router: Router) { }

    ngOnInit(): void {
        if (sessionStorage.getItem("userId") == null) {
            this.router.navigate([' ']);
        }
        this.updatedChildren = JSON.parse(sessionStorage.getItem("updatedChildren")!)
    }

    confirm() {
        this.childrenService.updateManyChildren(this.updatedChildren).subscribe((response: any) => {
            console.log(response);
            sessionStorage.removeItem('updatedChildren')
            this.router.navigate(['child-list']);
        });
    }

    cancel() {
        sessionStorage.removeItem('updatedChildren')
        this.router.navigate(['child-list']);
    }
}