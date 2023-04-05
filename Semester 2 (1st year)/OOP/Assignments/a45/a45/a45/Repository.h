#pragma once
#include "Event.h"
#include "DynamicVector.h"

class Repository
{
private:
	DynamicVector<Event> events;
public:
	Repository(DynamicVector<Event> events = NULL);
	DynamicVector<Event> getAllEvents();
	bool addEvent(Event eventToAdd);
	bool removeEvent(int positionToRemove);
	bool updateEvent(int positionToUpdate, Event newEvent);
	int findEventPosition(Event eventSearched);
};