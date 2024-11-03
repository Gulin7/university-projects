import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { ReservationService } from '../service/reservation.service';

@Component({
  selector: 'app-pick-list',
  standalone: true,
  imports: [],
  templateUrl: './pick-list.component.html',
  styleUrl: './pick-list.component.css',
})
export class PickListComponent {
  constructor(
    private router: Router,
    private reservationService: ReservationService
  ) {}
  flightList() {
    this.router.navigate(['flight-list']);
  }
  hotelList() {
    this.router.navigate(['hotel-list']);
  }
  cancelReservation() {
    this.reservationService.cancelReservation();
  }
}
