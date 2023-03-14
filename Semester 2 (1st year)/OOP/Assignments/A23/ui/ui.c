//
// Created by Tudor on 14/03/2023.
//

#include "ui.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>


UI *createUI(Service *service) {

    if (service == NULL)
        return NULL;

    UI *ui = (UI *) malloc(sizeof(UI));

    if (ui == NULL)
        return NULL;

    ui->service = service;

    return ui;
}

void destroyUI(UI *ui) {
    if (ui == NULL)
        return;
    destroyService(ui->service);
    free(ui);
}

void showMenu() {
    printf("        MENU\n"
           "1. Add a medicine\n"
           "2. Delete a medicine\n"
           "3. Update a medicine\n"
           "4. Display all medicines  \n"
           "5. Display all medicines which contain a given string\n"
           "6. Display all medicines short in supply \n"
           "7. Undo \n"
           "8. Redo \n"
           "9. Exit\n");
}

int getCommandInput() {
    int command;
    printf("Enter a command: ");
    scanf("%d", &command);
    return command;
}

char *getNameInput() {
    char *name = malloc(sizeof(char) * 100);

    printf("Enter a name: ");
    scanf(" %s", name);
    return name;
}

int getQuantityInput() {
    int quantity;
    printf("Enter a quantity: ");
    scanf("%d", &quantity);
    return quantity;
}

int getConcentrationInput() {
    int concentration;
    printf("Enter a concentration: ");
    scanf("%d", &concentration);
    return concentration;
}

double getPriceInput() {
    int price;
    printf("Enter a price: ");
    scanf("%d", &price);
    return price;
}

void addMedicine(UI *ui) {
    char *name = getNameInput();
    int concentration = getConcentrationInput();
    int quantity = getQuantityInput();
    double price = getPriceInput();

    addToService(ui->service, name, concentration, quantity, price);

    free(name);
}

void deleteMedicine(UI *ui) {
    char *name = getNameInput();
    int concentration = getConcentrationInput();

    deleteFromService(ui->service, name, concentration);

    free(name);
}

void updateMedicine(UI *ui) {
    char *name = getNameInput();
    int concentration = getConcentrationInput();
    int newQuantity = getQuantityInput();
    double newPrice = getPriceInput();

    updateInService(ui->service, name, concentration, newQuantity, newPrice);

    free(name);
}

void showAll(UI *ui) {
    MedicineRepository *repository = ui->service->repository;
    int lengthOfRepository = getSize(repository);
    for (int index = 0; index < lengthOfRepository; index++)
        toString(repository->medicines->elements[index]);
}

void showMedicinesContainingInputString(UI *ui) {
    char inputString[20];
    printf("Enter a string: ");
    scanf("%s", inputString);
    MedicineRepository *repository = ui->service->repository;
    int lengthOfRepository = getSize(repository);
    for (int index = 0; index < lengthOfRepository; index++) {
        if (strstr(getName(repository->medicines->elements[index]), inputString))
            toString(repository->medicines->elements[index]);
    }
}

void runUi(UI *ui) {
    generateMedicines(ui->service);

    while (1) {
        showMenu();

        int command = getCommandInput();

        //showAll(ui);

        switch (command) {
            case 1:
                addMedicine(ui);
                break;
            case 2:
                deleteMedicine(ui);
                break;
            case 3:
                updateMedicine(ui);
                break;
            case 4:
                showAll(ui);
                break;
            case 5:
                showMedicinesContainingInputString(ui);
                break;
            case 6:
                break;
            case 7:
                break;
            case 8:
                break;
            case 9:
                printf("You left the app!");
                return;
        }
    }
}