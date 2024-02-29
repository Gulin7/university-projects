#pragma once
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <algorithm>

using std::string;
using std::vector;

class Researcher
{
private:
	string name;
	string position;
public:
	Researcher(string name, string position) : name(name), position(position) {}

	string getName() { return this->name; }
	string getPosition() { return this->position; }

	string toStringShort() { return this->name + " " + this->position; }
	string toString() { return "Name: " + this->name + " | Position: " + this->position; }
	string toStringFile() { return this->name + ";" + this->position; }

	~Researcher() {}
};

