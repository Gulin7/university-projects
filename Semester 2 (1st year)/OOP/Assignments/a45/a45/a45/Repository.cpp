#include "Repository.h"

Repository::Repository(std::vector<Event> events) :
	events{events}
{
}

std::vector<Event> Repository::getAllEvents()
{
	return this->events;
}

bool Repository::addEvent(Event eventToAdd)
{
	auto iterator = std::find(this->events.begin(), this->events.end(), eventToAdd);
	if (iterator != this->events.end())
		return false;
	this->events.push_back(eventToAdd);
	return true;
}

bool Repository::removeEvent(int positionToRemove)
{
	if (positionToRemove < 0 || positionToRemove >= this->events.size())
		return false;
	this->events.erase(this->events.begin() + positionToRemove);
	return true;
}

bool Repository::updateEvent(int positionToUpdate, Event newEvent)
{
	if (positionToUpdate < 0 || positionToUpdate >= this->events.size())
		return false;
	this->events[positionToUpdate]= newEvent;
	return true;
}

int Repository::findEventPosition(Event eventSearched)
{
	auto iterator = std::find(this->events.begin(), this->events.end(), eventSearched);
	if (iterator == this->events.end())
		return -1;
	return std::distance(this->events.begin(), iterator);
}
