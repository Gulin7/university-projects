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
	bool addEventToRepository(Event eventToAdd);
	bool removeEventFromRepository(int positionToRemove);
	bool updateEventInRepository(int positionToUpdate, Event newEvent);
	int findEventPosition(Event eventSearched);
};