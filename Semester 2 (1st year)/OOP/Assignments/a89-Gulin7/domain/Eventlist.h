#pragma once
#include "Event.h"
#include <vector>

class Eventlist
{
protected:
	std::vector<Event> events;
public:
	Eventlist(std::vector<Event> initialEvents = {}) {};
	std::vector<Event> getAllEvents();
	bool addEvent(Event eventToAdd);
	bool removeEvent(Event eventToRemove);
	void setEvents(std::vector<Event> newEv) {
		events = newEv;
	}
	virtual ~Eventlist() {};
};
