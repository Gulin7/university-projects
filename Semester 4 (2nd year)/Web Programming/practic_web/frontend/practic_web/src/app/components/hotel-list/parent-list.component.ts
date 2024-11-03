import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ParentService } from '../../service/parent.service';
import { ReservationService } from '../../service/reservation.service';

@Component({
  selector: 'app-parent-list',
  templateUrl: './parent-list.component.html',
  styleUrls: ['./parent-list.component.css'],
  standalone: true,
  imports: [CommonModule],
})
export class ParentListComponent implements OnInit {
  parents: any[] = [];

  constructor(
    private parentService: ParentService,
    private router: Router,
    private reservationService: ReservationService
  ) {}

  ngOnInit(): void {
    if (
      sessionStorage.getItem('user') == null ||
      sessionStorage.getItem('date') == 'null' ||
      sessionStorage.getItem('destination') == 'null'
    ) {
      this.router.navigate([' ']);
    }
    var destination = sessionStorage.getItem('destination');
    var date = sessionStorage.getItem('date');
    if (date == null || destination == null) {
      return;
    }
    this.parentService
      .getHotelsByDateAndDestination(date, destination)
      .subscribe((parents) => {
        console.log(parents);
        this.parents = parents;
      });
  }

  refresh(): void {
    if (
      sessionStorage.getItem('user') == null ||
      sessionStorage.getItem('date') == null ||
      sessionStorage.getItem('destination') == null
    ) {
      this.router.navigate([' ']);
    }
    var destination = sessionStorage.getItem('destination');
    var date = sessionStorage.getItem('date');
    if (date == null || destination == null) {
      return;
    }
    this.parentService
      .getHotelsByDateAndDestination(date, destination)
      .subscribe((parents) => {
        console.log(parents);
        this.parents = parents;
      });
  }

  reserve(hotel: any) {
    var username = sessionStorage.getItem('username');
    var date = sessionStorage.getItem('date');
    if (username == null || date == null) {
      return;
    }
    var type = 'hotel';
    var type_id = hotel.h_id;
    console.log('reservation made');
    this.parentService
      .decreaseAvailable(hotel.h_id, (parseInt(hotel.available) - 1).toString())
      .subscribe(
        (response) => {
          console.log(response);
        },
        (error) => {
          console.error(error);
        }
      );
    this.reservationService
      .addReservation(username, date, type, type_id)
      .subscribe(
        (response) => {
          console.log(response);
        },
        (error) => {
          console.error(error);
        }
      );
  }

  flightList() {
    this.router.navigate(['flight-list']);
  }
  hotelList() {
    this.router.navigate(['hotel-list']);
  }
  cancelReservation() {
    this.reservationService.cancelReservation().subscribe(
      (response) => {
        console.log(response);
      },
      (error) => {
        console.error(error);
      }
    );
  }
}
