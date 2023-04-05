//
// Created by gulin on 05/04/2023.
//

#ifndef A235JUMA_DOMAIN_H
#define A235JUMA_DOMAIN_H

#include <stdlib.h>
#include <stdio.h>

/*
 * Struct that stores a medicine ( the main entity ).
 */
typedef struct {
    char *name;
    int quantity, concentration;
    double price;
} Medicine;

/*
 * Function that creates a Medicine object and allocates space for it and all it's fields.
 * :name: char, can be anything
 * :concentration: int, represents the concentration
 * :price: double, represents the price of the Medicine
 * :quantity: int, represents the quantity of Medicine
 */
Medicine *createMedicine(char *name, int concentration, int quantity, double price);

/*
 * Functions that destroys a Medicine and deallocates it's memory.
 * :medicine: pointer to a Medicine object
 */
void destroyMedicine(Medicine *medicine);

/*
 *
 */
Medicine *copyMedicine(Medicine *medicine);

/*
 * Getter for the Medicine objects name
 * :medicine: pointer to a Medicine object
 * :return:
 */
char *getName(Medicine *medicine);

/*
 * Getter for the Medicine concentration
 * :medicine: pointer to a Medicine object
 * :return:
 */
int getConcentration(Medicine *medicine);

/*
 * Getter for the Medicine quantity.
 * :medicine: pointer to a Medicine object
 * :return: const int
 */
int getQuantity(Medicine *medicine);

/*
 * Getter for the Medicine price.
 * :medicine: pointer to a Medicine object
 * :return: double
 */
double getPrice(Medicine *medicine);

/*
 * Prints the Medicine object as a string.
 */
void toString(Medicine *medicine);

#endif //A235JUMA_DOMAIN_H
