import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { ParentService } from '../../service/parent.service';
import { FormsModule } from '@angular/forms';

@Component({
    selector: 'app-parent-create',
    templateUrl: './parent-create.component.html',
    standalone: true,
    imports: [FormsModule],
    styleUrls: ['./parent-create.component.css']
})
export class ParentCreateComponent {
    parent = { name: '', userId: '' };

    constructor(private parentService: ParentService, private router: Router) { }

    ngOnInit(): void {
        if (sessionStorage.getItem("user") == null) {
            this.router.navigate([' ']);
        }
        this.parent.userId = sessionStorage.getItem("user")!;
    }

    createParent(): void {
        this.parentService.createParent(this.parent).subscribe(() => {
            this.router.navigate(['/parent-list']);
        });
    }
}