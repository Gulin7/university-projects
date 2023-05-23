#include "Car.h"
#include <string>

void Car::setManufacturer(std::string newManufacturer)
{
    this->manufacturer = newManufacturer;
}

void Car::setModel(std::string newModel)
{
    this->model = newModel;
}

void Car::setColour(std::string newColour)
{
    this->colour = newColour;
}

void Car::setFabricationYear(int newFabricationYear)
{
    this->fabricationYear = newFabricationYear;
}

std::string Car::getManufacturer()
{
    return this->manufacturer;
}

std::string Car::getModel()
{
    return this->model;
}

std::string Car::getColour()
{
    return this->colour;
}

int Car::getFabricationYear()
{
    return this->fabricationYear;
}

bool Car::operator==(Car& carToCheck)
{
    return this->model == carToCheck.getModel() && this->manufacturer == carToCheck.getManufacturer() && 
        this->fabricationYear == carToCheck.getFabricationYear() && this->colour == carToCheck.getColour();
}

void Car::operator=(Car& newCar)
{
    this->model = newCar.getModel();
    this->colour = newCar.getColour();
    this->manufacturer = newCar.getManufacturer();
    this->fabricationYear = newCar.getFabricationYear();
}

std::string Car::carToString()
{
    return "Manufacturer: " + this->manufacturer + " | Model: "+this->model+" | Colour: "+this->colour+" | FabricationYear: " + std::to_string(this->fabricationYear);
}

std::ostream& operator<<(std::ostream& outputFile, Car& carToWrite)
{
    // TODO: insert return statement here
    outputFile << carToWrite.carToString();
    return outputFile;
}
