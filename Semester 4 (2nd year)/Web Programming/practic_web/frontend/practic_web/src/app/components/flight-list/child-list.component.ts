import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ChildService } from '../../service/child.service';
import { ReservationService } from '../../service/reservation.service';

@Component({
  selector: 'app-child-list',
  templateUrl: './child-list.component.html',
  styleUrls: ['./child-list.component.css'],
  standalone: true,
  imports: [CommonModule],
})
export class ChildListComponent implements OnInit {
  children: any[] = [];

  constructor(
    private childService: ChildService,
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
    this.childService
      .getFlightsByDateAndDestination(date, destination)
      .subscribe((children) => {
        this.children = children;
      });
  }

  refresh(): void {
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
    this.childService
      .getFlightsByDateAndDestination(date, destination)
      .subscribe((children) => {
        this.children = children;
      });
  }

  reserve(flight: any) {
    var username = sessionStorage.getItem('username');
    var date = sessionStorage.getItem('date');
    if (username == null || date == null) {
      return;
    }
    var type = 'flight';
    var type_id = flight.f_id;
    this.childService
      .decreaseAvailable(
        flight.f_id,
        (parseInt(flight.available) - 1).toString()
      )
      .subscribe(
        (response) => {
          console.log(response);
        },
        (error) => {
          console.error(error);
        }
      );
    console.log('reservation made');
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
