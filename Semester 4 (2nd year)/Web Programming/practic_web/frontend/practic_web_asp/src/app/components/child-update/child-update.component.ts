import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { ChildService } from '../../service/child.service';

@Component({
  selector: 'app-child-update',
  templateUrl: './child-update.component.html',
  styleUrls: ['./child-update.component.css'],
  standalone: true,
  imports: [FormsModule],
})
export class ChildUpdateComponent implements OnInit {
  child = { id: '', name: '', rank: '' };
  id = '';

  constructor(
    private childService: ChildService,
    private router: Router,
    private route: ActivatedRoute
  ) {
    console.log('we got here');
  }

  ngOnInit(): void {
    if (sessionStorage.getItem('user') == null) {
      this.router.navigate([' ']);
    }
    this.id = this.route.snapshot.paramMap.get('id')!;
    this.child.id = this.id;
    console.log(this.id);
    this.childService.getChild(this.id).subscribe((child) => {
      this.child = child;
      console.log(this.child);
    });
    //console.log(this.child);
  }

  updateChild(): void {
    this.childService.updateChild(this.id, this.child).subscribe(() => {
      this.router.navigate(['/child-list']);
    });
  }
}
