#include "Repository.h"
#include <exception>
#include <iostream>

Repository::Repository(std::vector<Car> cars)
{
    this->cars = cars;
}

std::vector<Car> Repository::getAllCars()
{
    return this->cars;
}

void Repository::addCar(Car carToAdd)
{
    if (this->findCar(carToAdd.getModel(), carToAdd.getFabricationYear()) != -1)
        throw std::exception("Car exists!");
    this->cars.push_back(carToAdd);
}

void Repository::removeCar(std::string model, int fabricationYear)
{
    int position = this->findCar(model, fabricationYear);
    if (position == -1 || position > this->cars.size())
        throw std::exception("Car not existing!");
    this->cars.erase(this->cars.begin() + position);
}

int Repository::findCar(std::string model, int fabricationYear)
{
    for (int index = 0; index < this->cars.size();index++) {
        if (cars[index].getModel() == model && cars[index].getFabricationYear() == fabricationYear)
            return index;
    }
    return -1;
}

int Repository::getSize()
{
    return this->cars.size();
}
