#pragma once
#include "Repository.h"

class AdministratorService
{
private:
	Repository eventRepository;

public:
	AdministratorService(Repository eventRepository);
	bool addEvent(std::string title, std::string description, Date date, Time time, int numberOfPeople, std::string link);
	bool removeEvent(std::string title, std::string description);
	bool updateEvent(std::string title, std::string description, std::string newTitle, std::string newDescription, Date newDate, Time newTime, int newNumberOfPeople, std::string newLink);
	bool increaseNumberOfPeople(std::string title, std::string description);
	DynamicVector<Event> getAllEvents();
	void generateEvents();
	Date generateDate();
	Time generateTime();
};