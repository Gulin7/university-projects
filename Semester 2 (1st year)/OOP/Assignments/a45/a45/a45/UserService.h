#pragma once
#include "Repository.h"

class UserService {
private:
	Repository eventRepository;
	DynamicVector<Event> eventlist;
public:
	UserService(Repository events);
	bool addEventToList(Event eventToAdd);
	bool removeEventFromList(std::string title, std::string description);
	DynamicVector<Event> getEventOfGivenMonth(DynamicVector<Event> events, int month);
	DynamicVector<Event> getEventList();
};