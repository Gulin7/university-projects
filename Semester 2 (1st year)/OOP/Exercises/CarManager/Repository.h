#pragma once
#include "Car.h"

class Repository
{
private:
	std::vector<Car> cars;		
	std::string filename;
public:
	Repository(std::string filename, std::vector<Car> cars = {}) : filename(filename), cars(cars){}
	std::vector<Car> getAllCars();
	int findCar(Car carToFind);
	void addCar(Car carToAdd);
	void removeCar(Car carToRemove);
	std::vector<Car> getAllCarsByManufacturer(std::string givenManufacturer);
};

