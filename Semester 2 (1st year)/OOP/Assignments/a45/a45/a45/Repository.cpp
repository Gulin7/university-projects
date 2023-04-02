#include "Repository.h"

Repository::Repository(DynamicVector<Event> events) :
	events{events}
{
}

DynamicVector<Event> Repository::getAllEvents()
{
	return this->events;
}

bool Repository::addEventToRepository(Event eventToAdd)
{
	if (this->events.findPosition(eventToAdd) != -1)
		return false;
	this->events.addElement(eventToAdd);
	return true;
}

bool Repository::removeEventFromRepository(int positionToRemove)
{
	if (positionToRemove < 0 || positionToRemove >= this->events.getSize())
		return false;
	this->events.removeElement(positionToRemove);
	return true;
}

bool Repository::updateEventInRepository(int positionToUpdate, Event newEvent)
{
	if (positionToUpdate < 0 || positionToUpdate >= this->events.getSize())
		return false;
	this->events.updateElement(positionToUpdate, newEvent);
}

int Repository::findEventPosition(Event eventSearched)
{
	return this->events.findPosition(eventSearched);
}
