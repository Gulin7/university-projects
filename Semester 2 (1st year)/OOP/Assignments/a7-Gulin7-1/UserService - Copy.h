#pragma once
#include "Repository.h"
#include "FileEventlist.h"

class UserService {
private:
	Repository eventRepository;
	FileEventlist* eventlist;
public:
	UserService(Repository events, FileEventlist* eventslist);
	bool addEventToList(Event eventToAdd);
	bool removeEventFromList(std::string title, std::string description);
	std::vector<Event> getEventOfGivenMonth(std::vector<Event> events, int month);
	FileEventlist* getEventList();
	void saveEventlist();
	void openEventlist();
};