#include "Ui.h"

#define ADD_DEPARMENT 1
#define SHOW_ALL 2
#define SHOW_EFFICIENT 3
#define SAVE_TO_FILE 4
#define EXIT 0

void Ui::addDeparment()
{
	std::string hospitalName;
	int numberOfDoctors;
	int department;
	std::cout << "Enter 1 for surgery or 2 for neonatalunit: ";
	std::cin >> department;
	if (department == 1) {
		int numberOfPatients;
		std::cout << "Enter a hospital name: ";
		std::cin.ignore();
		std::getline(std::cin, hospitalName);
		std::cout << "Enter number of doctors: ";
		std::cin >> numberOfDoctors;
		std::cout << "Enter number of patients: ";
		std::cin >> numberOfPatients;
		HospitalDepartment* department = new Surgery(hospitalName, numberOfDoctors, numberOfPatients);
		this->controller.addDepartment(department);
	}
	else if (department == 2) {
		double averageGrade;
		std::cout << "Enter a hospital name: ";
		std::cin.ignore();
		std::getline(std::cin, hospitalName);
		std::cout << "Enter number of doctors: ";
		std::cin >> numberOfDoctors;
		std::cout << "Enter average grade: ";
		std::cin >> averageGrade;
		HospitalDepartment* department = new Surgery(hospitalName, numberOfDoctors, averageGrade);
		this->controller.addDepartment(department);
	}
	else {
		std::cout << "Invalid department type dummy!";
	}
}

void Ui::getAllDepartments()
{
	for (auto& deparment : this->controller.getAllDepartments())
		std::cout << deparment->toString();
}

void Ui::getAllEfficientDepartments()
{
	for (auto& deparment : this->controller.getAllEfficientDepartments())
		std::cout << deparment->toString();
}

void Ui::writeToFile()
{
	std::string filename;
	std::cout << "Enter a filename: ";
	std::cin.ignore();
	std::getline(std::cin, filename);
	this->controller.writeToFile(filename);
}

int Ui::getCommand()
{
	int command;
	while (true) {
		std::cout << "Enter a command: ";
		std::cin >> command;
		if (command < 0 || command > 5)
			std::cout << "Invalid command!\n";
		else {
			return command;
		}
	}
	
}

void Ui::showMenu()
{
	std::cout << "\n	MENU\n";
	std::cout << "1.Add department\n";
	std::cout << "2.Show all\n";
	std::cout << "3.Show efficient\n";
	std::cout << "4.Save to file\n";
	std::cout << "0.Exit\n";
}

void Ui::runUi()
{
	while (true) {
		this->showMenu();
		int command = this->getCommand();
		switch (command) {
		case ADD_DEPARMENT:
			this->addDeparment();
			break;
		case SHOW_ALL:
			this->getAllDepartments();
			break;
		case SHOW_EFFICIENT:
			this->getAllEfficientDepartments();
			break;
		case SAVE_TO_FILE:
			this->writeToFile();
			break;
		case EXIT:
			std::cout << "You left the app!";
			return;
		default:
			std::cout << "Something went wrong!";
			break;
		}
	}
}
