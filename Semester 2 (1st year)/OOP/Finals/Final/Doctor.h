#pragma once
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <algorithm>

using std::string;
using std::vector;
class Doctor
{
private:
	string name, specialisation;
public:
	Doctor(string name, string specialisation): name(name), specialisation(specialisation){}
	string getName() { return this->name; }
	string getSpecialisation() { return this->specialisation; }
	void setName(string name) { this->name = name; }
	void setSpecialisation(string specialisation) { this->specialisation = specialisation; }

	string toString() { return "Name: " + this->name + " | Specialisation: " + this->specialisation; }

	string toStringFile(){ return this->name + ";" + this->specialisation; }
};

