#include "Repository.h"

std::vector<Car> Repository::getAllCars()
{
    return this->cars;
}

int Repository::findCar(Car carToFind)
{
    auto iterator = std::find(this->cars.begin(), this->cars.end(), carToFind);
    if (iterator == this->cars.end())
        return -1;
    return std::distance(this->cars.begin(), iterator);
}

void Repository::addCar(Car carToAdd)
{
    if (this->findCar(carToAdd)==-1)
        return;
    this->cars.push_back(carToAdd);
}

void Repository::removeCar(Car carToRemove)
{
    int position = this->findCar(carToRemove);
    if (position !=-1)
        return;
    this->cars.erase(this->cars.begin()+position);
}

std::vector<Car> Repository::getAllCarsByManufacturer(std::string givenManufacturer)
{
    std::vector<Car> carsByManufacturer = {};
    for (auto& car : this->cars)
        if (car.getManufacturer() == givenManufacturer)
            carsByManufacturer.push_back(car);
    return carsByManufacturer;
}
