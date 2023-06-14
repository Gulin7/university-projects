#pragma once

#include <string>
#include <vector>

#include "Answer.h"

using std::string;
using std::vector;

class AnswerRepository
{
private:
	vector<Answer> answersDatabase;

	int currentId;
	string filePath;

public:
	AnswerRepository(string filePath);
	
	void readFile();

	int findAnswer(int id);
	void addAnswer(Answer answerToAdd);
	vector<Answer>& getAll();
	int getCurrentId();
	Answer& getAnswerById(int id);
};

