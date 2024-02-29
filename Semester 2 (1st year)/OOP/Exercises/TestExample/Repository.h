#pragma once
#include "Car.h"
#include <vector>
#include <string>

class Repository {
private:
	std::vector<Car> cars;
public:
	Repository(std::vector<Car> cars = {});
	std::vector<Car> getAllCars();
	void addCar(Car carToAdd);
	void removeCar(std::string model, int fabricationYear);
	void updateCar(std::string model, int fabricationYear, Car newCar);
	int findCarPosition(std::string model, int fabricationYear);
};