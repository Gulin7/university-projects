#pragma once
#include "Service.h"
#include <iostream>

#define ADD_CAR 1
#define REMOVE_CAR 2
#define SHOW_CARS 3
#define VINTAGE_CARS 4
#define EXIT 0

class Ui {
private:
	Service service;
public:
	Ui(Service service);
	int getCommand();
	std::string inputModel();
	std::string inputManufacturer();
	std::string inputColour();
	int inputFabricationYear();

	void showMenu();
	void runUi();

	void addCar();
	void removeCar();
	void showAllCars();
	void showVintageCars();

};