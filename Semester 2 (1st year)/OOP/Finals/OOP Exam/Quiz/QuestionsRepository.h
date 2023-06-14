#pragma once

#include <vector>

#include "Question.h"

using std::vector;

class QuestionsRepository
{
private:
	vector<Question> questions;
	string filePath;

public:
	QuestionsRepository(const string& filePath);

	void readFile();
	void writeFile();

	Question& getQuestionAtPosition(int position);
	int findById(int id);
	void add(Question questionToAdd);
	vector<Question>& getAll();
};

