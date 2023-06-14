#include "QuestionsRepository.h"
#include "stringOperations.h"

#include <algorithm>
#include <exception>
#include <fstream>

using std::ifstream;


QuestionsRepository::QuestionsRepository(string filePath) : filePath{ filePath }
{
    this->currentId = 0;
    this->readFile();
}

void QuestionsRepository::readFile()
{
	int maxId = -1;

	ifstream inputFile{ this->filePath };

	if (!inputFile.is_open())
	{
		throw std::exception{ "Failed to open file!" };
	}

	string currentQuestion;

	while (getline(inputFile, currentQuestion))
	{
		vector<string> fields = splitString(currentQuestion, '|');

		if (fields.size() != 3)
			continue;

		int id = stoi(fields[0]);

		if (id > maxId)
			maxId = id;

		Question questionToAdd(stoi(fields[0]), fields[1], fields[2]);

		this->addQuestion(questionToAdd);
	}

	inputFile.close();

	this->currentId = maxId + 1;
}

int QuestionsRepository::findQuestion(int id)
{
	auto position = find_if(
		this->questionsDatabase.begin(),
		this->questionsDatabase.end(),
		[id](Question currentQuestion)
		{
			return currentQuestion.getId() == id;
		});

	if (position == this->questionsDatabase.end())
		return -1;

	return position - this->questionsDatabase.begin();
}

void QuestionsRepository::addQuestion(Question questionToAdd)
{
	if (this->findQuestion(questionToAdd.getId()) != -1)
		throw std::exception{ "Question already in repository!" };

	this->questionsDatabase.push_back(questionToAdd);
	currentId++;
}

int QuestionsRepository::findByDescription(string description)
{
	for (int i = 0; i < this->questionsDatabase.size(); i++)
		if (questionsDatabase[i].getText() == description)
			return questionsDatabase[i].getId();

	return -1;
}

int QuestionsRepository::getCurrentId()
{
	return this->currentId;
}

vector<Question>& QuestionsRepository::getAll()
{
	return this->questionsDatabase;
}
