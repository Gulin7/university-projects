#include "Subject.h"

void Subject::registerObserver(Observer* observerToRegister)
{
	this->observers.push_back(observerToRegister);
}

void Subject::notify()
{
	for (auto& observer : observers)
		observer->update();
}
