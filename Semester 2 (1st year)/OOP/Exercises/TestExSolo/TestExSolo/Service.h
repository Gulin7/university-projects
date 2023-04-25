#pragma once
#include "Repository.h"

class Service {
private:
	Repository repository;
public:
	Service(Repository repository);

	std::vector<Car> getAllCars();
	void addCar(Car carToAdd);
	void removeCar(std::string model, int fabricationYear);
	int findPosition(std::string model, int fabricationYear);
	std::vector<Car> getVintageCars();
	void generateCars();
};