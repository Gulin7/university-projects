#pragma once

#include <string>

using std::string;

class Idea
{
private:
	string description, status, creator;
	int act;

public:
	Idea(string description, string status, string creator, int act);

	string getDescription();
	string getStatus();
	string getCreator();
	int getAct();

	void setStatus(string newStatus);
};

