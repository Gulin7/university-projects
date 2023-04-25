#pragma once
#include "Repository.h"
#include "Service.h"
#include <assert.h>
#include <iostream>
#include <string>
#include <vector>

class Ui
{
private:
	int a;
public:
	Ui(Service service);
	void showMenu();
	void showAll();
	
	int inputCommand();
};

