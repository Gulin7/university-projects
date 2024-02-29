#include "Car.h"

Car::Car(std::string manufacturer, std::string model, int fabricationYear, std::string colour)
{
	this->manufacturer = manufacturer;
	this->model =model ;
	this->fabricationYear =fabricationYear ;
	this->colour = colour ;
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

bool Car::operator==(Car carToCheck)
{
	return (this->colour == carToCheck.getColour() && this->fabricationYear == carToCheck.getFabricationYear() && this->manufacturer == carToCheck.getManufacturer() && this->model == carToCheck.getModel());
}

void Car::operator=(Car newCar)
{
	this->colour = newCar.getColour();
	this->fabricationYear = newCar.getFabricationYear();
	this->manufacturer = newCar.getManufacturer();
	this->model = newCar.getModel();
}
