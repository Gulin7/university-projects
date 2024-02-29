#include "Eventlist.h"

std::vector<Event> Eventlist::getAllEvents()
{
    return this->events;
}

bool Eventlist::addEvent(Event eventToAdd)
{
    auto iterator = std::find(this->events.begin(), this->events.end(), eventToAdd);
    if (iterator != this->events.end())
        return false;
    this->events.push_back(eventToAdd);
    return true;
}

bool Eventlist::removeEvent(Event eventToRemove)
{
    auto iterator = std::find(this->events.begin(), this->events.end(), eventToRemove);
    if (iterator == this->events.end())
        return false;
    this->events.erase(iterator);
    return true;
}
