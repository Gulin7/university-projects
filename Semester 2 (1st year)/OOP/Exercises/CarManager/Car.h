#pragma once
#include <string.h>
#include <vector>
#include <assert.h>
#include <iostream>
#include <ostream>

class Car
{
private:
	std::string manufacturer;
	std::string model;
	std::string colour;
	int fabricationYear;

public:
	Car() : manufacturer(""), model(""), colour(""), fabricationYear(2023) {}
	Car(std::string manufacturer, std::string model, std::string colour, int fabricationYear) :
		manufacturer(manufacturer), model(model), colour(colour), fabricationYear(fabricationYear) {}
	void setManufacturer(std::string newManufacturer);
	void setModel(std::string newModel);
	void setColour(std::string newColour);
	void setFabricationYear(int newFabricationYear);

	std::string getManufacturer();
	std::string getModel();
	std::string getColour();
	int getFabricationYear();

	bool operator==(Car& carToCheck);
	void operator=(Car& newCar);

	friend std::istream& operator>>(std::istream& inputFile, Car& carToRead);
	friend std::ostream& operator<<(std::ostream& outputFile, Car& carToWrite);

	std::string carToString();

};

