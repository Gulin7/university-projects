#include "Medicine.h"
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

#define _CRT_SECURE_NO_WARNINGS

Medicine createMedicine(char *name, int concentration, int quantity, float price) {
    Medicine medicine;

    if (name == NULL || concentration <= 0 || quantity <= 0) {
        return medicine;
    }

    medicine.name = malloc((strlen(name) + 1) * sizeof(char));
    medicine.concentration = concentration;
    medicine.quantity = quantity;
    medicine.price = price;

    return medicine;
}

char *getName(Medicine medicine) {
    return medicine.name;
}

int getConcentration(Medicine medicine) {
    return medicine.concentration;
}

int getQuantity(Medicine medicine) {
    return medicine.quantity;
}

float getPrice(Medicine medicine) {
    return medicine.price;
}

void setName(Medicine *medicine, char *name) {
    free(medicine->name);
    medicine->name = malloc((strlen(name) + 1) * sizeof(char));
    strcpy(medicine->name, name);
}

void setConcentration(Medicine *medicine, int concentration) {
    medicine->concentration = concentration;
}

void setQuantity(Medicine *medicine, int quantity) {
    medicine->quantity = quantity;
}

void setPrice(Medicine *medicine, float price) {
    medicine->price = price;
}

Medicine copyMedicine(Medicine medicine) {
    Medicine newMedicine;
    newMedicine = createMedicine(getName(medicine), getConcentration(medicine), getQuantity(medicine),
                                 getPrice(medicine));
    return newMedicine;
}

void destroyMedicine(Medicine medicine) {
    free(medicine.name);
}
