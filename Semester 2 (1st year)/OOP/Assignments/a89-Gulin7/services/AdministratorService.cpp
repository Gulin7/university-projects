#include "AdministratorService.h"
#include "Validator.h"

AdministratorService::AdministratorService(Repository* eventRepository) :
	eventRepository{ eventRepository }
{
}

Repository* AdministratorService::getRepo()
{
	return this->eventRepository;
}

bool AdministratorService::addEvent(std::string title, std::string description, Date date, Time time, int numberOfPeople, std::string link)
{
	Event eventToAdd{ title, description, date, time, numberOfPeople, link };
	return this->eventRepository->addEvent(eventToAdd);
}

bool AdministratorService::removeEvent(std::string title, std::string description)
{
	Date date;
	date.day = 1;
	date.month = 1;
	date.year = 2023;
	Time time;
	time.minute = 0;
	time.hour = 0;
	Event eventToRemove{ title, description,date,time, 0, "" };
	int positionToRemove = this->eventRepository->findEventPosition(eventToRemove);
	return this->eventRepository->removeEvent(positionToRemove);
}

bool AdministratorService::updateEvent(std::string title, std::string description, std::string newTitle, std::string newDescription, Date newDate, Time newTime, int newNumberOfPeople, std::string newLink)
{
	Date date;
	date.day = 1;
	date.month = 1;
	date.year = 2023;
	Time time;
	time.minute = 0;
	time.hour = 0;
	Event eventToUpdate{ title, description, date, time, 0, "" };
	Event eventUpdated{ newTitle, newDescription, newDate, newTime, newNumberOfPeople, newLink };
	int positionToUpdate = this->eventRepository->findEventPosition(eventToUpdate);
	return this->eventRepository->updateEvent(positionToUpdate, eventUpdated);
}

bool AdministratorService::increaseNumberOfPeople(std::string title, std::string description)
{
	Date date;
	date.day = 1;
	date.month = 12;
	date.year = 2023;
	Time time;
	time.hour = 0;
	time.minute = 1;
	Event eventToFind{ title, description, date, time, 0, "" };
	int position = this->eventRepository->findEventPosition(eventToFind);
	Event eventToUpdate = this->eventRepository->getAllEvents()[position];
	Event eventUpdated{ title, description, eventToUpdate.getDate(), eventToUpdate.getTime(), eventToUpdate.getNumberOfPeople() + 1, eventToUpdate.getLink() };
	return this->eventRepository->updateEvent(position, eventUpdated);
}

void AdministratorService::decreaseNumberOfPoeple(std::string title, std::string description)
{
	Date date;
	date.day = 1;
	date.month = 12;
	date.year = 2023;
	Time time;
	time.hour = 0;
	time.minute = 1;
	Event eventToFind{ title, description, date, time, 0, "" };
	int position = this->eventRepository->findEventPosition(eventToFind);
	Event eventToUpdate = this->eventRepository->getAllEvents()[position];
	Event eventUpdated{ title, description, eventToUpdate.getDate(), eventToUpdate.getTime(), eventToUpdate.getNumberOfPeople() - 1, eventToUpdate.getLink() };
}

std::vector<Event> AdministratorService::getAllEvents()
{
	return this->eventRepository->getAllEvents();
}

Event AdministratorService::getEventByTitle(std::string title)
{
	Event newEvent;
	for (auto& event : this->getAllEvents()) {
		if (title == event.getTitle())
		{
			newEvent.setDate(event.getDate());
			newEvent.setDescription(event.getDescription());
			newEvent.setLink(event.getLink());
			newEvent.setTime(event.getTime());
			newEvent.setNumberOfPeople(event.getNumberOfPeople());
			newEvent.setTitle(event.getTitle());
			return newEvent;
		}
	}
	Date date;
	Time time;
	date.day = 1;
	date.month = 1;
	date.year = 1;
	time.hour = 1;
	time.minute = 1;
	Event emptyEvent{ "","",date, time,1,"" };
	return emptyEvent;
}

void AdministratorService::generateEvents()
{
	Date date;
	Time time;

	date = generateDate();
	time = generateTime();
	this->addEvent("CodeFlight", "Cool event!", date, time, 0, "https://www.facebook.com/events/");

	date = generateDate();
	time = generateTime();
	this->addEvent("InoHub", "Cool event!", date, time, 0, "https://www.facebook.com/events/");

	date = generateDate();
	time = generateTime();
	this->addEvent("Hermes Hackathon", "Cool event!", date, time, 0, "https://www.facebook.com/events/");

	date = generateDate();
	time = generateTime();
	this->addEvent("Kitsch Party", "Cool event!", date, time, 0, "https://www.facebook.com/events/");

	date = generateDate();
	time = generateTime();
	this->addEvent("Pool Party", "Cool event!", date, time, 0, "https://www.facebook.com/events/");

	date = generateDate();
	time = generateTime();
	this->addEvent("Movie Night", "Cool event!", date, time, 0, "https://www.facebook.com/events/");

	date = generateDate();
	time = generateTime();
	this->addEvent("Spuma Party", "Cool event!", date, time, 0, "https://www.facebook.com/events/");

	date = generateDate();
	time = generateTime();
	this->addEvent("CFR vs UCluj", "Cool event!", date, time, 0, "https://www.facebook.com/events/");

	date = generateDate();
	time = generateTime();
	this->addEvent("Cluj Days", "Cool event!", date, time, 0, "https://www.facebook.com/events/");

	date = generateDate();
	time = generateTime();
	this->addEvent("Cluj Marathon", "Cool event!", date, time, 0, "https://www.facebook.com/events/");

}

Date AdministratorService::generateDate()
{
	Date date;
	date.day = rand() % 29;
	date.month = rand() % 13;
	int randomNumber = rand() % 3;
	if (randomNumber % 3 == 0)
		date.year = 2023;
	else if (randomNumber % 3 == 1)
		date.year = 2024;
	else
		date.year = 2025;
	return date;
}

Time AdministratorService::generateTime()
{
	Time time;
	time.minute = rand() % 60;
	time.hour = rand() % 24;
	return time;
}
