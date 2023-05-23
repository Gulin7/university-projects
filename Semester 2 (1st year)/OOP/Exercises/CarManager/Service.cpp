#include "Service.h"

std::vector<Car> Service::getAllCars()
{
	return this->repo.getAllCars();
}

std::vector<Car> Service::getAllCarsByManufacturer(std::string manufacturer)
{
	return this->repo.getAllCarsByManufacturer(manufacturer);
}
