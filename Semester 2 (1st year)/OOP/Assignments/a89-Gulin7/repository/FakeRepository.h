#pragma once
#include "Event.h"
#include <vector>
#include "Repository.h"

class FakeRepository :
	public Repository
{
private:
public:
	FakeRepository() {};
	bool boolValue = true;
	bool addEvent(Event eventToAdd) override;
	bool removeEvent(int positionToRemove) override;
	bool updateEvent(int positionToUpdate, Event newEvent) override;
	std::vector<Event> getAllEvents() override;
private:
};

