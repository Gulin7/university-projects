#include "Question.h"

string Question::toString()
{
	string questionString = "Id: " + std::to_string(id) + " | Text: " + text + " | Answer: " + answer + " | Score: " + std::to_string(score);
	return questionString;
}

string Question::toStringNoAnswer()
{
	string questionString = "Id: " + std::to_string(id) + " | Text: " + text + " | Score: " + std::to_string(score);
	return questionString;
}

string Question::toStringFile()
{
	string questionString = std::to_string(id) + ";" + text + ";" + answer + ";" + std::to_string(score);
	return questionString;
}
