#include "Ui.h"

Ui::Ui(Service service): service{service}
{
}

int Ui::getCommand()
{
	int command;
	while (true) {
		std::cout << "\nEnter a command: ";
		std::cin >> command;
		if (std::cin.fail() || command < 0 || command>4) {
			std::cout << "\nInvalid command!";
			std::cin.clear();
			std::cin.ignore(std::numeric_limits < std::streamsize >::max(), '\n');
			continue;
		}
		else
			break;
	}
	return command;
}

int Ui::getCommand()
{
	int command;
	while (true) {
		std::cout << "\nEnter a command: ";
		std::cin >> command;
		if (std::cin.fail() || command < 0 || command>4) {
			std::cout << "\nInvalid command!";
			std::cin.clear();
			std::cin.ignore(std::numeric_limits < std::streamsize >::max(), '\n');
			continue;
		}
		else
			break;
	}
	return command;
}

std::string Ui::inputModel()
{
	std::string model;
	std::cout << "\nEnter a model: ";
	std::cin.ignore();
	std::getline(std::cin, model);
	return model;
}

std::string Ui::inputManufacturer()
{
	std::string manufacturer;
	std::cout << "\nEnter a manufacturer: ";
	std::cin.ignore();
	std::getline(std::cin, manufacturer);
	return manufacturer;
}

std::string Ui::inputColour()
{
	std::string colour;
	std::cout << "\nEnter a colour: ";
	std::cin.ignore();
	std::getline(std::cin, colour);
	return colour;
}

int Ui::inputFabricationYear()
{
	int fabricationYear;
	while (true) {
		std::cout << "\nEnter a fabrication year: ";
		std::cin >> fabricationYear;
		if (std::cin.fail() || fabricationYear < 1800) {
			std::cout << "\nInvalid fabrication year!";
			std::cin.clear();
			std::cin.ignore(std::numeric_limits < std::streamsize >::max(), '\n');
			continue;
		}
		else
			break;
	}
	return fabricationYear;
}

void Ui::showMenu()
{
	std::cout << "			MENU		" ;
	std::cout << "\n1.Add a car.";
	std::cout << "\n2.Remove a car.";
	std::cout << "\n3.Show all cars.";
	std::cout << "\n4.Show all vintage cars.";
	std::cout << "\n0.Exit.\n";
}

void Ui::runUi()
{
	int command;
	while (true)
	{
		showMenu();
		command = getCommand();
		try{
			switch (command)
			{
			case ADD_CAR:
				this->addCar();
				break;
			case REMOVE_CAR:
				this->removeCar();
				break;
			case SHOW_CARS:
				this->showAllCars();
				break;
			case VINTAGE_CARS:
				this->showVintageCars();
				break;
			case EXIT:
				std::cout << "Application exited successfully!";
				std::cout << std::endl;
				return;
			default:
				std::cout << "\nInvalid option! Please try again!\n\n";
				break;
			}
		}
		catch (std::exception& e) {
			std::cout << "\n" << e.what() << "\n";
		}
	}
}

void Ui::addCar()
{
	std::string manufacturer = this->inputManufacturer();
	std::string model = this->inputModel();
	int fabricationYear = this->inputFabricationYear();
	std::string colour = this->inputColour();
	Car carToAdd{ manufacturer,model,fabricationYear,colour };
	this->service.addCar(carToAdd);
}

void Ui::removeCar()
{
	std::string model = this->inputModel();
	int fabricationYear = this->inputFabricationYear();
	this->service.removeCar(model, fabricationYear);
}

void Ui::showAllCars()
{
	std::vector<Car> cars= this->service.getAllCars();
	for (int index = 0;index<cars.size();index++) {
		std::cout << "\n#"<<index<<"\n";
		std::cout << "Manufacturer: " << cars[index].getManufacturer() << "\n";
		std::cout << "Model: " << cars[index].getModel() << "\n";
		std::cout << "Fabrication year: " << cars[index].getFabricationYear() << "\n";
		std::cout << "Colour: " << cars[index].getColour() << "\n";
	}
}

void Ui::showVintageCars()
{
	std::vector<Car> cars = this->service.getVintageCars();
	for (int index = 0; index < cars.size(); index++) {
		std::cout << "\n#" << index << "\n";
		std::cout << "Manufacturer: " << cars[index].getManufacturer() << "\n";
		std::cout << "Model: " << cars[index].getModel() << "\n";
		std::cout << "Fabrication year: " << cars[index].getFabricationYear() << "\n";
		std::cout << "Colour: " << cars[index].getColour() << "\n";
	}
}
