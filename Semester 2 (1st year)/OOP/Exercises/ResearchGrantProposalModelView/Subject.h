#pragma once
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <algorithm>
#include "Observer.h"

using std::string;
using std::vector;

class Subject
{
private:
	vector<Observer*> observers;
public:
	void addObserver(Observer* obs) {
		observers.push_back(obs);
	}	
	void notify() {
		for (auto& obs : observers)
			obs->update();
	}
};
