#include "FakeRepository.h"

bool FakeRepository::addEvent(Event eventToAdd)
{
    return boolValue;
}

bool FakeRepository::removeEvent(int positionToRemove)
{
    return boolValue;
}

bool FakeRepository::updateEvent(int positionToUpdate, Event newEvent)
{
    return boolValue;
}

std::vector<Event> FakeRepository::getAllEvents()
{
    std::vector<Event> events;
    Date date1 = Date{ 2023,10,2 };
    Time time1 = Time{ 10,10 };
    Event event1{ "NACHO", "CEL MAI TARE", date1, time1, 3, "www.youtube.com" };
    Event event2{ "NACHO2", "CEL MAI TARE!", date1, time1, 3, "www.youtube.com" };
    events.push_back(event1);
    events.push_back(event2);
    return events;
}
