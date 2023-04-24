#include "Repository.h"

Repository::Repository(std::vector<Car> cars)
{
}

std::vector<Car> Repository::getAllCars()
{
    return cars;
}

void Repository::addCar(Car carToAdd)
{
    int position = this->findCarPosition(carToAdd.getModel(), carToAdd.getFabricationYear());
    if (position == -1)
        throw "Not existing car!";
    this->cars.push_back(carToAdd);
}

void Repository::removeCar(std::string model, int fabricationYear)
{
    int position= this->findCarPosition(model, fabricationYear);
    if (position == -1)
        throw "Not existing car!";
    this->cars.erase(this->cars.begin() + this->findCarPosition(model, fabricationYear));
}

void Repository::updateCar(std::string model, int fabricationYear, Car newCar)
{
    int position = this->findCarPosition(model, fabricationYear);
    if (position == -1)
        throw "Not existing car!";
    this->cars[position] = newCar;
}

int Repository::findCarPosition(std::string model, int fabricationYear)
{
    for (int index = 0; index< this->cars.size();index++) {
        if (cars[index].getModel() == model && cars[index].getFabricationYear() == fabricationYear)
            return index;
    }
    return -1;
}
