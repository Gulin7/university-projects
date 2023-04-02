#include "Event.h"
#include <iostream>

Event::Event(std::string title, std::string description, Date date, Time time, int numberOfPeople, std::string link)
{
	this->title = title;
	this->description = description;
	this->date = date;
	this->time = time;
	this->numberOfPeople = numberOfPeople;
	this->link = link;
}

std::string Event::getTitle()
{
	return this->title;
}

std::string Event::getDescription()
{
	return this->description;
}

Date Event::getDate()
{
	return this->date;
}

Time Event::getTime()
{
	return this->time;
}

int Event::getNumberOfPeople()
{
	return this->numberOfPeople;
}

std::string Event::getLink()
{
	return this->link;
}

void Event::setTitle(std::string newTitle)
{
	this->title = newTitle;
}

void Event::setDescription(std::string newDescription)
{
	this->description = newDescription;
}

void Event::setDate(Date newDate)
{
	this->date = newDate;
}

void Event::setTime(Time newTime)
{
	this->time = newTime;
}

void Event::setNumberOfPeople(int newNumberOfPeople)
{
	this->numberOfPeople = newNumberOfPeople;
}

void Event::setLink(std::string newLink)
{
	this->link = newLink;
}

bool Event::operator==(const Event& eventToCheck)
{
	if (this->title == eventToCheck.title && this->description == eventToCheck.description)
		return true;
	return false;
}

void Event::operator=(const Event& eventToCopy)
{
	this->title = eventToCopy.title;
	this->description = eventToCopy.description;
	this->date = eventToCopy.date;
	this->time = eventToCopy.time;
	this->link = eventToCopy.link;
}

void Event::showEvent()
{
	std::cout << "Title: " << this->title << std::endl;
	std::cout << "Description: " << this->description<< std::endl;
	std::cout << "Date: " << this->date.day << ":" << this->date.month << ":" << this->date.year << std::endl;
	std::cout << "Time: " << this->time.hour << ":" << this->time.minute << std::endl;
	std::cout << "Number of people: " << this->numberOfPeople << std::endl;
	std::cout << "Link: " << this->link << std::endl;
}
