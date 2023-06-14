#pragma once

#include <string>

using std::string;

class User
{
private:
	string name, type;

public:
	User(){}
	User(string name, string type);

	string getName();
	string getType();
};

