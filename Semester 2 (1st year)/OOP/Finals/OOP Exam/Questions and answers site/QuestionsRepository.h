#pragma once

#include "Question.h"

#include <vector>

using std::vector;

class QuestionsRepository
{
private:
	vector<Question> questionsDatabase;
	int currentId;

	string filePath;

public:
	QuestionsRepository(string filePath);

	void readFile();

	int findQuestion(int id);
	void addQuestion(Question questionToAdd);

	int findByDescription(string description);

	int getCurrentId();

	vector<Question>& getAll();
};

