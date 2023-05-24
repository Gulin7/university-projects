#include "Event.h"
#include <iostream>
#include "Tools.h"
#include <vector>

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

std::istream& operator>>(std::istream& inputFile, Event& eventToRead)
{
	std::string lineRead;
	getline(inputFile, lineRead);
	std::vector<std::string> tokens = tokenize(lineRead, ',');
	if (tokens.size() != 6)
		return inputFile;
	eventToRead.title = tokens[0];
	eventToRead.description = tokens[1];
	std::vector<std::string> dateTokens = tokenize(tokens[2], ':');
	if (dateTokens.size() != 3)
		return inputFile;
	eventToRead.date = Date{ std::stoi(dateTokens[0]), std::stoi(dateTokens[1]), std::stoi(dateTokens[2])};
	std::vector<std::string> timeTokens = tokenize(tokens[3], ':');
	if (timeTokens.size() != 2)
		return inputFile;
	eventToRead.time = Time{ std::stoi(timeTokens[0]), std::stoi(timeTokens[1]) };
	eventToRead.numberOfPeople = std::stoi(tokens[4]);
	eventToRead.link = tokens[5];
	return inputFile;
}

std::ostream& operator<<(std::ostream& outputFile, const Event& eventToWrite)
{
	outputFile << eventToWrite.title << "," << eventToWrite.description << "," << eventToWrite.date.day << ":" << eventToWrite.date.month << ":" << eventToWrite.date.year << "," << eventToWrite.time.hour << ":" << eventToWrite.time.minute << ":" << eventToWrite.numberOfPeople << "," << eventToWrite.link << "\n";
	return outputFile;
}
