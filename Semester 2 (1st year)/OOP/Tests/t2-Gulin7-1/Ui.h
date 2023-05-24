#pragma once
#include <vector>
#include <string>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <exception>
#include "Controller.h"

class Ui
{
private:
	Controller controller;
public:
	Ui(Controller newController) : controller{ newController } {};
	void addDeparment();
	void getAllDepartments();
	void getAllEfficientDepartments();
	void writeToFile();
	int getCommand();
	void showMenu();
	void runUi();
};

