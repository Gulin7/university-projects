#pragma once
#include "Event.h"
#include <vector>
#include "Exception.h"

class Eventlist
{
protected:
	std::vector<Event> events;
public:
	Eventlist(std::vector<Event> initialEvents = {}) {};
	std::vector<Event> getAllEvents();
	bool addEvent(Event eventToAdd);
	bool removeEvent(Event eventToRemove);
	virtual ~Eventlist() {};
};
