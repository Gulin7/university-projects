#pragma once
#include "Repository.h"
#include "FileEventlist.h"

class UserService {
private:
	FileEventlist* eventlist;
public:
	Repository* eventRepository;
	UserService(Repository* events, FileEventlist* eventslist);
	bool addEventToList(Event eventToAdd);
	bool removeEventFromList(std::string title, std::string description);
	std::vector<Event> getEventOfGivenMonth(std::vector<Event> events, int month);
	FileEventlist* getEventList();
	void saveEventlist();
	std::string getFilename() {
		return this->eventlist->getFilename();
	}
	void setFilename(std::string newFilename) {
		this->eventlist->setFilename(newFilename);
	}
	void openEventlist();
};