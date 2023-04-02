#include "UserService.h"

UserService::UserService(Repository events) :
	eventRepository{events}
{
}

bool UserService::addEventToList(Event eventToAdd)
{
	if (this->eventlist.findPosition(eventToAdd) != -1)
		return false;

	this->eventlist.addElement(eventToAdd);
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
	int position = this->eventlist.findPosition(event);
	if (position < 0 || position >= this->eventlist.getSize())
		return false;
	this->eventlist.removeElement(position);
	return true;

}

DynamicVector<Event> UserService::getEventOfGivenMonth(DynamicVector<Event> events, int month)
{
	DynamicVector <Event> eventsFound;
	int size = events.getSize();
	for (int index = 0; index < size; index++)
	{
		Event event = events.getElement(index);
		if (event.getDate().month == month)
			eventsFound.addElement(event);

	}
	return eventsFound;
}

DynamicVector<Event> UserService::getEventList()
{
	return this->eventlist;
}
