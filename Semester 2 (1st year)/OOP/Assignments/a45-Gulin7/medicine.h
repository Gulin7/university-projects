#pragma once

#include <stdio.h>
#include <stdlib.h>

/*
* Struct that defines the main entity.
*/
typedef struct {
	char* name;
	int concentration;
	int quantity;
	double price;
}Medicine;

/*
* Function that creates a medicine and allocates memory for it and it's fields.
* name: pointer to char
* concentration: int
* quantity: int
* price: double
*/
Medicine* createMedicine(char* name, int concentration, int quantity, double price);

/*
* Function that destroys a medicine and deallocates it's memory and it's fields.
* medicine: Medicine
*/
void destroyMedicine(Medicine* medicine);

/*
* Copies a medicine.
*/
Medicine* copyMedicine(Medicine* medicine);

/*
* 
*/
const char* getName(Medicine* medicine);

/*
* 
*/
const int getConcentration(Medicine* medicine);

/*
* 
*/
int getQuantity(Medicine* medicine);

/*
* 
*/
double getPrice(Medicine* medicine);

/*
* 
*/
void toString(Medicine* medicine);