#pragma once
#include "Car.h"
#include <vector>

class Repository {
private:
	std::vector<Car> cars;
public:
	Repository(std::vector<Car> cars = {});
	
	std::vector<Car> getAllCars();
	void addCar(Car carToAdd);
	void removeCar(std::string model, int fabricationYear);
	int findCar(std::string model, int fabricationYear);
	int getSize();
};