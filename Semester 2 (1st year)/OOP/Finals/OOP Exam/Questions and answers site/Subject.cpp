#include "Subject.h"

void Subject::registerObserver(Observer* observerToAdd)
{
	this->observers.push_back(observerToAdd);
}

void Subject::notify()
{
	for (auto& observer : this->observers)
		observer->update();
}
