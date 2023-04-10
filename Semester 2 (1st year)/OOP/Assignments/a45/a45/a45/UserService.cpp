#include "UserService.h"

UserService::UserService(Repository events) :
	eventRepository{events}
{
}

bool UserService::addEventToList(Event eventToAdd)
{
	auto iterator = std::find(this->eventlist.begin(), this->eventlist.end(), eventToAdd);
	if (iterator != this->eventlist.end())
		return false;

	this->eventlist.push_back(eventToAdd);
	return true;
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
	auto iterator = std::find(this->eventlist.begin(), this->eventlist.end(), event);
	if (iterator == this->eventlist.end())
		return false;
	this->eventlist.erase(iterator);
	return true;

}

std::vector<Event> UserService::getEventOfGivenMonth(std::vector<Event> events, int month)
{
	std::vector <Event> eventsFound;
	int size = events.size();
	for (int index = 0; index < size; index++){
		Event event = events[index];
		if (event.getDate().month == month)
			eventsFound.push_back(event);
	}
	return eventsFound;
}

std::vector<Event> UserService::getEventList()
{
	return this->eventlist;
}
