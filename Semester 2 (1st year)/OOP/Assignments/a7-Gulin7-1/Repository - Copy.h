#pragma once
#include "Event.h"
#include <vector>

class Repository
{
private:
	std::vector<Event> events;
	std::string filename;
public:
	Repository(std::string filename, std::vector<Event> events = {});
	std::vector<Event> getAllEvents();
	bool addEvent(Event eventToAdd);
	bool removeEvent(int positionToRemove);
	bool updateEvent(int positionToUpdate, Event newEvent);
	int findEventPosition(Event eventSearched);
private:
	void readFromFile();
	void writeToFile();
};