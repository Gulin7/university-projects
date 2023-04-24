#include "Car.h"
#include< fstream >
#include <istream>
#include <iostream>
#include <string>

Car::Car(std::string manufacturer, std::string model, int fabricationYear, std::string colour)
{
	this->manufacturer = manufacturer;
	this->model = model;
	this->colour = colour;
	this->fabricationYear = fabricationYear;
}

std::string Car::getManufacturer()
{
	return this->manufacturer;
}

std::string Car::getModel()
{
	return this->model;
}

int Car::getFabricationYear()
{
	return this->fabricationYear;
}

std::string Car::getColour()
{
	return this->colour;
}

void Car::setManufacturer(std::string newManufacturer)
{
	this->manufacturer = newManufacturer;
}

void Car::setModel(std::string newModel)
{
	this->model = newModel;
}

void Car::setFabricationYear(int newFabricationYear)
{
	this->fabricationYear = newFabricationYear;
}

void Car::setColour(std::string newColour)
{
	this->colour = newColour;
}

bool Car::operator==(const Car& carToCheck)
{
	if (this->manufacturer == carToCheck.manufacturer && this->model == carToCheck.model && 
		this->fabricationYear == carToCheck.fabricationYear && this->colour == carToCheck.colour)
		return true;
	return false;
}

void Car::operator=(const Car& carToCopy)
{
	this->colour = carToCopy.colour;
	this->fabricationYear = carToCopy.fabricationYear;
	this->model = carToCopy.model;
	this->manufacturer = carToCopy.manufacturer;
}
