#pragma once

#include <string>

using std::string;

class Participant
{
private:
	string name;
	int score;

public:
	Participant(const string& name);

	int getScore();
	string getName();

	void setScore(int newScore);
};

