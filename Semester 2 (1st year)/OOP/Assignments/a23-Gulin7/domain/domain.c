//
// Created by Tudor on 14/03/2023.
//
#define _CRT_SECURE_NO_WARNINGS

#include <string.h>
#include "domain.h"

Medicine *createMedicine(char *name, int concentration, int quantity, double price) {

    Medicine *medicine = (Medicine *) malloc(sizeof(Medicine));
    if (medicine == NULL) {
        return NULL;
    }

    medicine->name = malloc(sizeof(char) * (strlen(name) + 1));
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
    if (medicine == NULL) {
        return;
    }
    free(medicine->name);
    free(medicine);
}

Medicine *copyMedicine(Medicine *medicine) {
    Medicine *medicine1 = createMedicine(medicine->name, medicine->concentration, medicine->quantity, medicine->price);
    return medicine1;
}

char *getName(Medicine *medicine) {
    if (medicine == NULL) {
        return NULL;
    }
    return medicine->name;
}

int getConcentration(Medicine *medicine) {
    if (medicine == NULL) {
        return -1;
    }
    return medicine->concentration;
}


int getQuantity(Medicine *medicine) {
    if (medicine == NULL) {
        return -1;
    }
    return medicine->quantity;
}

double getPrice(Medicine *medicine) {
    if (medicine == NULL) {
        return -1;
    }
    return medicine->price;
}

void toString(Medicine *medicine) {
    printf("The medicine name is %s; the concentration is %d; the quantity is %d; the price is %.2f.\n", medicine->name,
           medicine->concentration, medicine->quantity, medicine->price);
}