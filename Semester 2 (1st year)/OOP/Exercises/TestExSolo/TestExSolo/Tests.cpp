#include "Tests.h"
#include <assert.h>
#include <iostream>

void Tests::testCar()
{
	/*
	CREATE A CAR AND CHECK IF IT WAS CREATED PROPERLY
	*/
	Car car{ "Mercedes", "E", 2000, "red" };
	assert(car.getColour() == "red");
	assert(car.getFabricationYear() == 2000);
	assert(car.getManufacturer() == "Mercedes");
	assert(car.getModel() == "E");
	/*
	TEST THE OPERATORS*/
	Car carToCheck{ "Mercedes", "E", 2000, "red" };
	assert(car == carToCheck);
	Car newCar{ "Mercedes", "C", 2005, "blue" };
	carToCheck = newCar;
	assert(carToCheck == newCar);
	/*
	TEST THE SETTERS*/
	car.setColour(newCar.getColour());
	car.setFabricationYear(newCar.getFabricationYear());
	car.setManufacturer(newCar.getManufacturer());
	car.setModel(newCar.getModel());
	assert(car == newCar);
}

void Tests::testRepository()
{
	std::vector<Car> initialCars = {};
	Repository repository{ initialCars };
	Car car{ "Mercedes", "E", 2000, "red" };
	Car newCar{ "Mercedes", "C", 2005, "blue" };
	/*
	Assert add + getSize + find */
	assert(repository.getSize() == 0);
	repository.addCar(car);
	assert(repository.getSize() == 1);
	assert(repository.findCar(car.getModel(), car.getFabricationYear()) == 0);
	assert(repository.findCar(newCar.getModel(), newCar.getFabricationYear()) == -1);
	repository.addCar(newCar);
	assert(repository.getSize() == 2);
	assert(repository.findCar(newCar.getModel(), newCar.getFabricationYear()) == 1);
	/*
	Assert remove */
	repository.removeCar(car.getModel(), car.getFabricationYear());
	assert(repository.getSize() == 1);
}

void Tests::testService()
{
	std::vector<Car> initialCars = {};
	Repository repository{ initialCars };
	Car car{ "Mercedes", "E", 1960, "red" };
	Car car2{ "Mercedes", "G", 1960, "black" };
	Car newCar{ "Mercedes", "C", 2005, "blue" };
	Service service{ repository };
	/*
	* ASSERT EMPTY 
	*/
	assert(service.getVintageCars().size() == 0);
	assert(service.getAllCars().size() == 0);
	/*
	* ASSERT ADD + FIND
	*/
	assert(service.findPosition(car.getModel(), car.getFabricationYear()) == -1);
	service.addCar(car);
	assert(service.findPosition(car.getModel(), car.getFabricationYear()) == 0);
	assert(service.getVintageCars().size() == 1);
	assert(service.getAllCars().size() == 1);
	service.addCar(newCar);
	assert(service.getAllCars().size() == 2);
	assert(service.getVintageCars().size() == 1);
	assert(service.getAllCars()[0] == newCar);
	/*
	* ASSERT VINTAGE CARS SORTED
	*/
	service.addCar(car2);
	assert(service.getVintageCars().size() == 2);
	assert(service.getVintageCars()[0] == car2);
	assert(service.getVintageCars()[1] == car);
	/*
	* ASSERT REMOVE
	*/
	service.removeCar(car2.getModel(), car2.getFabricationYear());
	assert(service.findPosition(car2.getModel(), car2.getFabricationYear()) == -1);
}

void Tests::testAll()
{
	std::cout << "Tests started!\n";
	testCar();
	testRepository();
	testService();
	std::cout << "Tests passed!\n";
}
