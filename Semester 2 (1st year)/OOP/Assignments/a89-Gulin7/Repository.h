#pragma once
#include "Event.h"
#include <vector>

class Repository
{
private:
	std::vector<Event> events;
	std::string filename;
public:
	Repository(std::string filename="Events.txt", std::vector<Event> events = {});
	virtual std::vector<Event> getAllEvents();
	virtual bool addEvent(Event eventToAdd);
	virtual bool removeEvent(int positionToRemove);
	virtual bool updateEvent(int positionToUpdate, Event newEvent);
	int findEventPosition(Event eventSearched);
private:
	void readFromFile();
	void writeToFile();
};