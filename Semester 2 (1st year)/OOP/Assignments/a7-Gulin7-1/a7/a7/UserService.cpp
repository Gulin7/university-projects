#include "UserService.h"

UserService::UserService(Repository events, FileEventlist* eventslist) :
	eventRepository{ events },
	eventlist{eventslist}
{
}

bool UserService::addEventToList(Event eventToAdd)
{
	return this->eventlist->addEvent(eventToAdd);
}


bool UserService::removeEventFromList(std::string title, std::string description)
{
	Date date;
	date.day = 1;
	date.month = 1;
	date.year = 2023;
	Time time;
	time.hour = 0;
	time.minute = 0;
	Event event{ title, description, date, time, 0, "" };
	if (this->eventlist == nullptr)
		return false;
	return this->eventlist->removeEvent(event);
}

std::vector<Event> UserService::getEventOfGivenMonth(std::vector<Event> events, int month){
	std::vector <Event> eventsFound;
	int size = 0;
	size = events.size();
	for (int index = 0; index < size; index++) {
		Event event = events[index];
		if (event.getDate().month == month)
			eventsFound.push_back(event);
	}
	return eventsFound;
}

FileEventlist* UserService::getEventList()
{
	return this->eventlist;
}

void UserService::saveEventlist()
{
	this->eventlist->writeToFile();

}

void UserService::openEventlist()
{
	this->eventlist->displayEvents();
}
