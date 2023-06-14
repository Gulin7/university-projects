#pragma once

#include <string>

using std::string;

class ScreenWriter
{
private:
	string name, expertise;

public:
	ScreenWriter(string name, string expertise);

	string getName();
	string getExpertise();
};

