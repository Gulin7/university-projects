#pragma once
#include "Observer.h"
#include <vector>

class Subject
{
private:
	std::vector<Observer*> observers;
public:
	void addObserver(Observer* observer) { this->observers.push_back(observer); }
	void notify() {
		for (auto& observer : observers)
			observer->update();
	}
};

