#pragma once

#include <string>

using std::string;

class Answer
{
private:
	int id, questionId, numberOfVotes;
	string userName, answerText;

public:
	Answer(int id, int questionId, int numberOfVotes, string userName, string answerText);

	int getId();
	int getQuestionId();
	int getNumberOfVotes();
	string getUserName();
	string getAnswerText();

	void setNumberOfVotes(int newNumberOfVotes);

	string toString();
};

