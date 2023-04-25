#pragma once
#include <string>

class Car {
private:
	std::string manufacturer;
	std::string model;
	int fabricationYear;
	std::string colour;
public:
	Car(): manufacturer(""), model(""), fabricationYear(0), colour("") {}
	Car(std::string manufacturer, std::string model, int fabricationYear, std::string colour);
	std::string getManufacturer();
	std::string getModel();
	int getFabricationYear();
	std::string getColour();

	void setManufacturer(std::string newManufacturer);
	void setModel(std::string newModel);
	void setFabricationYear(int newFabricationYear);
	void setColour(std::string newColour);

	bool operator==(Car carToCheck);
	void operator=(Car newCar);
};