//
// Created by gulin on 29/03/2023.
//

#ifndef A23_VOI_TRECE_PRIN_MONITOR_MEDICINE_H
#define A23_VOI_TRECE_PRIN_MONITOR_MEDICINE_H

#include <stdio.h>
#include <stdlib.h>

/*
 * Struct that stores a medicine.
 */
typedef struct {
    char *name;
    int quantity, concentration;
    double price;
} Medicine;

/*
 * Function that creates a Medicine object and allocates space for it and all it's fields.
 * name: pointer to char
 * concentration: int
 * quantity: int
 * price: double
 */
Medicine *createMedicine(char *name, int concentration, int quantity, double price);

/*
 * Function that destroys a medicine and deallocates it's memory.
 * medicine: pointer to a Medicine object
 */
void destroyMedicine(Medicine *medicine);

/*
 * Creates a copy of a medicine and returns that copy.
 */
Medicine *copyMedicine(Medicine *medicine);

/*
 *
 */
const char *getName(Medicine *medicine);

/*
 *
 */
const int getConcentration(Medicine *medicine);

/*
 *
 */
int getQuantity(Medicine *medicine);

/*
 *
 */
double getPrice(Medicine *medicine);

/*
 *
 */
void toString(Medicine *medicine);

#endif //A23_VOI_TRECE_PRIN_MONITOR_MEDICINE_H
