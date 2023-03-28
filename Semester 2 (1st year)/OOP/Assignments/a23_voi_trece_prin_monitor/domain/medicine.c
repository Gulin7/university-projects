//
// Created by gulin on 29/03/2023.
//

#include "medicine.h"
#include <string.h>

Medicine *createMedicine(char *name, int concentration, int quantity, double price) {
    if (name == NULL)
        return NULL;

    Medicine *medicine = (Medicine *) malloc(sizeof(Medicine));
    if (medicine == NULL)
        return NULL;

    medicine->name = malloc(sizeof(char) * strlen(name) + 1);
    if (medicine->name == NULL) {
        free(medicine);
        return NULL;
    }

    strcpy(medicine->name, name);

    medicine->concentration = concentration;
    medicine->quantity = quantity;
    medicine->price = price;
    return medicine;
}

void destroyMedicine(Medicine *medicine) {
    if (medicine == NULL)
        return;

    free(medicine->name);
    free(medicine);
}

Medicine *copyMedicine(Medicine *medicine) {
    Medicine *newMedicine = createMedicine(medicine->name, medicine->concentration, medicine->quantity,
                                           medicine->price);
    return newMedicine;
}

const char *getName(Medicine *medicine) {
    if (medicine == NULL)
        return NULL;

    return medicine->name;
}

const int getConcentration(Medicine *medicine) {
    if (medicine == NULL)
        return -1;

    return medicine->concentration;
}

int getQuantity(Medicine *medicine) {
    if (medicine == NULL)
        return -1;

    return medicine->quantity;
}

double getPrice(Medicine *medicine) {
    if (medicine == NULL)
        return -1;

    return medicine->price;
}

void toString(Medicine *medicine) {
    printf("Name: %s, concentration: %d, quantity: %d, price: %.2f ", medicine->name, medicine->concentration,
           medicine->quantity, medicine->price);
}
