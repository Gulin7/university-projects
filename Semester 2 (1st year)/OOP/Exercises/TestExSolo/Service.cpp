#include "Service.h"
#include <algorithm>

bool compareManufacturerModel(Car& car1, Car& car2) {
	if (car1.getManufacturer() < car2.getManufacturer())
		return 1;
	else if (car1.getManufacturer() == car2.getManufacturer()) {
		if (car1.getModel() < car2.getModel())
			return 1;
	}
	return 0;
}

bool compareColours(Car& car1, Car& car2) {
	if (car1.getColour() < car2.getColour())
		return 1;
	return 0;
}

Service::Service(Repository repository)
{
	this->repository = repository;
}

std::vector<Car> Service::getAllCars()
{
	std::vector<Car> cars = this->repository.getAllCars();
	std::sort(cars.begin(), cars.end(), compareManufacturerModel);
	return cars;
}

void Service::addCar(Car carToAdd)
{
	this->repository.addCar(carToAdd);
}

void Service::removeCar(std::string model, int fabricationYear)
{
	this->repository.removeCar(model, fabricationYear);
}

int Service::findPosition(std::string model, int fabricationYear)
{
	return this->repository.findCar(model, fabricationYear);
}

std::vector<Car> Service::getVintageCars()
{
	std::vector<Car> vintageCars = {};
	std::vector<Car> cars = this->getAllCars();

	for (int index = 0; index < cars.size();index++) {
		int fabricationYear = cars[index].getFabricationYear();
		if ((2023 - fabricationYear) >= 45)
			vintageCars.push_back(cars[index]);
	}
	std::sort(vintageCars.begin(), vintageCars.end(), compareColours);
	return vintageCars;
}

void Service::generateCars()
{
	Car car1{ "Dacia", "Logan", 2003, "red" };
	Car car2{ "Mercedes", "E", 2021, "purple" };
	Car car3{ "BMW", "Series3", 2013, "white" };
	Car car4{ "Audi", "A4", 1963, "blue" };
	Car car5{ "Bugatti", "Bolide", 2023, "black" };
	this->repository.addCar(car1);
	this->repository.addCar(car2);
	this->repository.addCar(car3);
	this->repository.addCar(car4);
	this->repository.addCar(car5);
}
