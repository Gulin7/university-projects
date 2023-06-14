#include "Idea.h"

Idea::Idea(string description, string status, string creator, int act) :
    description{ description }, status{ status }, creator{ creator }, act{ act }
{
}

string Idea::getDescription()
{
    return this->description;
}

string Idea::getStatus()
{
    return this->status;
}

string Idea::getCreator()
{
    return this->creator;
}

int Idea::getAct()
{
    return this->act;
}

void Idea::setStatus(string newStatus)
{
    this->status = newStatus;
}
