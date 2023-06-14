#include "Participant.h"

Participant::Participant(const string& name) : name{ name }
{
	this->score = 0;
}

int Participant::getScore()
{
	return this->score;
}

string Participant::getName()
{
	return this->name;
}

void Participant::setScore(int newScore)
{
	this->score = newScore;
}
