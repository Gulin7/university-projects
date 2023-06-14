#pragma once

#include <string>

using std::string;

class Question
{
private:
	int id, score;
	string text, correctAnswer;

public:
	Question(int id, string text, string correctAnswer, int score);

	int getId();
	int getScore();
	string getText();
	string getCorrectAnswer();

	string toString();
};

