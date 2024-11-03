import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ParentService } from '../../service/parent.service';
import { FormsModule } from '@angular/forms';

@Component({
    selector: 'app-parent-update',
    templateUrl: './parent-update.component.html',
    standalone: true,
    imports: [FormsModule],
    styleUrls: ['./parent-update.component.css']
})
export class ParentUpdateComponent implements OnInit {
    parent = { name: '', id: '', userId: '' };
    id = "";

    constructor(
        private parentService: ParentService,
        private router: Router,
        private route: ActivatedRoute
    ) { }

    ngOnInit(): void {
        if (sessionStorage.getItem("user") == null) {
            this.router.navigate([' ']);
        }
        this.id = this.route.snapshot.params['id'];
        this.parent.id = this.id;
        this.parent.userId = sessionStorage.getItem("user")!;
        this.parentService.getParent(this.id).subscribe(parent => {
            this.parent = parent;
        });
    }

    updateParent(): void {
        this.parentService.updateParent(this.parent).subscribe(() => {
            this.router.navigate(['/parent-list']);
        });
    }
}