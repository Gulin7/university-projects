#pragma once
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <algorithm>

using std::string;
using std::vector;

class Idea
{
private:
	string title;
	string description;
	string status;
	string creator;
	int duration;
public:
	Idea(string title, string description, string status, string creator, int duration) :
		title(title), description(description), status(status), creator(creator), duration(duration) {}

	string toStringShort() { return this->title + " " + this->description + " " + this->status + " " + this->creator + " " + std::to_string(this->duration); }
	//string toString() { return "Name: " + this->name + " | Position: " + this->position; }
	string toStringFile() { return this->title + ";" + this->description + ";" + this->status + ";" + this->creator + ";" + std::to_string(this->duration); }

	string getTitle() { return this->title; }
	string getDescription() { return this->description; }
	string getStatus() { return this->status; }
	string getCreator() { return this->creator; }
	int getDuration() { return this->duration; }

	void setDescription(string newDescription) { this->description = newDescription; }

	void setStatus(string newStatus) { this->status = newStatus; }

	~Idea() {}
};

