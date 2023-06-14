#pragma once

#include <string>

using std::string;

class User
{
private:
	string name;

public:
	User(string name) : name{ name } {}

	void setName(string newName);
	string getName();
};

