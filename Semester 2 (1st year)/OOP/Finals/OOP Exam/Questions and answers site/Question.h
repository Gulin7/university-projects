#pragma once

#include <string>

using std::string;

class Question
{
private:
	int id;
	string text, userName;

public:
	Question(int id, string text, string userName) : id{ id }, text{ text }, userName{ userName } {};
	Question() {}
	int getId();
	string getText();
	string getUserName();
};

