//
// Created by gulin on 05/04/2023.
//
#include "ui.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

Ui *createUI(Service *service) {

    if (service == NULL)
        return NULL;

    Ui *ui = (Ui *) malloc(sizeof(Ui));

    if (ui == NULL)
        return NULL;

    ui->service = service;

    return ui;
}

void destroyUI(Ui *ui) {
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
    if (scanf("%d", &command) != 1) {
        command = -1;
        while (getchar() != '\n') {}
        printf("Invalid input. Please enter a valid command.\n");
        return getCommandInput();
    }
    if (command > 9 || command < 1) {
        printf("Invalid input. Please enter a valid command.");
        return getCommandInput();
    }
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
    printf("Enter your quantity: ");
    if (scanf("%d", &quantity) != 1) {
        quantity = -1;
        while (getchar() != '\n') {}
        printf("Invalid input. Please enter a valid quantity.\n");
        return getQuantityInput();
    }
    if (quantity < 0) {
        printf("Invalid input. Please enter a valid quantity.\n");
        return getQuantityInput();
    }
    return quantity;
}

int getConcentrationInput() {
    int concentration;
    printf("Enter your concentration: ");
    if (scanf("%d", &concentration) != 1) {
        concentration = -1;
        while (getchar() != '\n') {}
        printf("Invalid input. Please enter a valid concentration.\n");
        return getConcentrationInput();
    }
    if (concentration < 0) {
        printf("Invalid input. Please enter a valid concentration.\n");
        return getConcentrationInput();
    }
    return concentration;
}

double getPriceInput() {
    int price;
    printf("Enter your price: ");
    if (scanf("%d", &price) != 1) {
        price = -1;
        while (getchar() != '\n') {}
        printf("Invalid input. Please enter a valid price.\n");
        return getPriceInput();
    }
    if (price <= 0) {
        printf("Invalid input. Please enter a valid price.\n");
        return getPriceInput();
    }
    return price;
}

void addMedicine(Ui *ui) {
    char *name = getNameInput();
    int concentration = getConcentrationInput();
    int quantity = getQuantityInput();
    double price = getPriceInput();

    addToService(ui->service, name, concentration, quantity, price);

    free(name);
}

void deleteMedicine(Ui *ui) {
    char *name = getNameInput();
    int concentration = getConcentrationInput();

    deleteFromService(ui->service, name, concentration);

    free(name);
}

void updateMedicine(Ui *ui) {
    char *name = getNameInput();
    int concentration = getConcentrationInput();
    int newQuantity = getQuantityInput();
    double newPrice = getPriceInput();

    updateInService(ui->service, name, concentration, newQuantity, newPrice);

    free(name);
}

void showAll(Ui *ui) {
    MedicineRepository *repository = ui->service->repository;
    int lengthOfRepository = getSize(repository);
    for (int index = 0; index < lengthOfRepository; index++)
        toString(repository->medicines->elements[index]);
}

void showMedicinesContainingInputString(Ui *ui) {
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

void showMedicineShortInSupply(Ui *ui) {
    int supply;
    printf("Enter a supply: ");
    scanf("%d", &supply);
    for (int index = 0; index < getServiceSize(ui->service); index++)
        if (getQuantity(ui->service->repository->medicines->elements[index]) < supply)
            toString(ui->service->repository->medicines->elements[index]);
}

void runUi(Ui *ui) {
    generateMedicines(ui->service);

    while (1) {
        showMenu();

        int command = getCommandInput();
        int outcome = 0;
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
                showMedicineShortInSupply(ui);
            case 7:
                outcome = undoOperation(ui->service);
                if (outcome == 0) {
                    printf("There are no more operations to undo!\n");
                }
                break;
            case 8:
                outcome = redoOperation(ui->service);
                if (outcome == 0) {
                    printf("There are no more operations to redo!\n");
                }
                break;
            case 9:
                printf("You left the app!");
                return;
        }
    }
}
