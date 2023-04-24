#pragma once
#include "Repository.h"

class UserService {
private:
	Repository eventRepository;
	std::vector<Event> eventlist;
public:
	UserService(Repository events);
	bool addEventToList(Event eventToAdd);
	bool removeEventFromList(std::string title, std::string description);
	std::vector<Event> getEventOfGivenMonth(std::vector<Event> events, int month);
	std::vector<Event> getEventList();
};