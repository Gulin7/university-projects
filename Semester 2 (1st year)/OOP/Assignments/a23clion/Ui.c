#include "Ui.h"
#include <stdio.h>
#include <string.h>
#include "Service.h"
#include "Repository.h"
#include "Medicine.h"
#include <stdlib.h>
#define _CRT_SECURE_NO_WARNINGS

Ui createUi(Service* service)
{
	Ui ui;
	ui.service = service;
	return ui;
}

void printMedicine(Medicine medicine) {
	printf("Name: %s\n", medicine.name);
	printf("Concentration: %d\n", medicine.concentration);
	printf("Quantity: %d\n", medicine.quantity);
	printf("Price: %.2f\n", medicine.price);
}

void showMenu() {
	printf("              MENU            \n");
	printf("1. Add medicine! \n");
	printf("2. Delete medicine! \n");
	printf("3. Update medicine! \n");
	printf("4. Display medicines in stock! \n");
	printf("5. Display medicines on quantity! \n");
	printf("6. Undo! \n");
	printf("7. Redo! \n");
	printf("0. Exit! \n");
}

int isNumber(char* string) {
	char digits[] = "0123456789";
	int number = 0;
	for (int index = 0; index < strlen(string); index++) {
		if (strchr(digits, string[index]) == NULL)
			return -1;
		number = number * 10 + (int)string[index];
	}
	return number;
}

int getCommandInput() {
	char* command[2];
	printf("Enter a concentration: ");
	scanf("%s", &command);
	int number = isNumber(command);
	return number;
}

char* getNameInput() {
	char* name[100];
	while (1) {
		printf("Enter a name: ");
		scanf("%s", &name);
		if (name == NULL)
			printf("Huh?\n");
		else
			break;
	}
	return name;
}

int getConcentrationInput() {
	char* concentration[5];
	printf("Enter a concentration: ");
	scanf("%s", &concentration);
	int number = isNumber(concentration);
	return number;
}

int getQuantityInput() {
	char* quantity[5];
	printf("Enter a quantity: ");
	scanf("%s", &quantity);
	int number = isNumber(quantity);
	return number;
}

float getPriceInput() {
	float price;
	printf("Enter a price: ");
	scanf("%f", &price);
	return price;
}

void runUi(Ui ui)
{
	generateMedicines(ui.service);
	int command=0;
	while (1) {
		showMenu();
		command = getCommandInput();
		if (command < 0 || command>7) {
			printf("Invalid command!");
			continue;
		}
		else if (command == 0) {
			printf("You left the app!");
			destroyService(ui.service);
			return;
		}
		else if (command == 1) {
			char* name = getNameInput();
			int concentration = getConcentrationInput();
			int quantity = getQuantityInput();
			float price = getPriceInput();
			if (concentration < 0 || quantity < 0) {
				printf("Invalid input!");
				continue;
			}
			addMedicineService(ui.service, name, concentration, quantity, price);
			sortMedicinesByName(ui.service->repository);
			addUndo(ui.service->undoRedo, name, concentration, quantity, price, 1);
			deleteRedoService(ui.service);
		}
		else if (command == 3) {
			char* name = getNameInput();
			int concentration = getConcentrationInput();
			int quantity = getQuantityInput();
			float price = getPriceInput();
			if (concentration < 0 || quantity < 0) {
				printf("Invalid input!");
				continue;
			}
			int position = findMedicine(ui.service->repository, name, concentration);
			int lastQuantity = getQuantity(ui.service->repository->medicines[position]);
			float lastPrice = getPrice(ui.service->repository->medicines[position]);
			updateMedicineService(ui.service, name, concentration, quantity, price);
			addUndo(ui.service, name, concentration, lastQuantity, lastPrice, 3);
			deleteRedoService(ui.service);
		}
		else if (command == 2) {
			char* name = getNameInput();
			int concentration = getConcentrationInput();
			if (concentration < 0) {
				printf("Invalid input!");
				continue;
			}
			int position = findMedicine(ui.service->repository, name, concentration);
			int quantity = ui.service->repository->medicines[position].quantity;
			float price = ui.service->repository->medicines[position].price;
			deleteMedicineService(ui.service, name, concentration);
			addUndo(ui.service->undoRedo, name, concentration, quantity, price, 2);
			deleteRedoService(ui.service);
		}
		else if (command == 4) {
			char partialString[20];
			printf("Enter a partial string: ");
			scanf("%s", &partialString);
			if (partialString == "\n")
				for (int index = 0; index < getSizeRepository(ui.service->repository); index++)
					printMedicine(ui.service->repository->medicines[index]);
			else {
				int total = 0;
				for (int index = 0; index < getSizeRepository(ui.service->repository); index++)
					if (strstr(getMedicinesService(ui.service), partialString) != NULL)
					{
						printMedicine(ui.service->repository->medicines[index]);
						total++;
					}
				if (total == 0)
					printf("No medicines found!\n");
			}
		}
		else if (command == 5) {
			printf("Show all the medicines low on stock!\n");
			int quantity = getQuantityInput();
			for (int index = 0; index < getSizeRepository(ui.service->repository); index++)
			{
				if (getQuantity(ui.service->repository->medicines[index]) <= quantity)
					printMedicine(ui.service->repository->medicines[index]);
			}
		}
		else if (command == 6) {
			int result = undo(ui.service);
			if (result == 0)
				printf("Operation undone!");
			else
				printf("There is no operation to undo!");
			printf("\n");
		}
		else if (command == 7) {
			int result = redo(ui.service);
			if (result == 0)
				printf("Gg!");
			else
				printf("There is no operation to redo!");
			printf("\n");
		}
	}
	return;
}
