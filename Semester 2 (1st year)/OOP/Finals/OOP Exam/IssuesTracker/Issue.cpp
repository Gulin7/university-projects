#include "Issue.h"

Issue::Issue(string description, string status, string reporter, string solver) :
	description{ description }, status{ status }, reporter{ reporter }, solver{ solver }
{
}

string Issue::getDescription()
{
	return this->description;
}

string Issue::getStatus()
{
	return this->status;
}

string Issue::getReporter()
{
	return this->reporter;
}

string Issue::getSolver()
{
	return this->solver;
}

string Issue::toString()
{
	return this->getDescription() + "|" + this->getStatus() + "|" + this->getReporter() + "|" + this->getSolver();
}

void Issue::setSolver(string newSolver)
{
	this->solver = newSolver;
}

void Issue::setStatus(string newStatus)
{
	this->status = newStatus;
}
