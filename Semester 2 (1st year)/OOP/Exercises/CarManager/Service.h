#pragma once
#include "Repository.h"
#include <vector>
#include "Car.h"

class Service
{
private:
	Repository repo;
public:
	Service(Repository repo) : repo(repo) {};
	std::vector<Car> getAllCars();
	std::vector<Car> getAllCarsByManufacturer(std::string manufacturer);
};

