#include "AnswerRepository.h"
#include "stringOperations.h"

#include <algorithm>
#include <exception>
#include <fstream>

using std::ifstream;

AnswerRepository::AnswerRepository(string filePath) : filePath{ filePath }
{
	this->currentId = 0;

	this->readFile();
}

void AnswerRepository::readFile()
{
	int maxId = -1;

	ifstream inputFile{ this->filePath };

	if (!inputFile.is_open())
	{
		throw std::exception{ "Failed to open file!" };
	}

	string currentAnswer;

	while (getline(inputFile, currentAnswer))
	{
		vector<string> fields = splitString(currentAnswer, '|');

		if (fields.size() != 5)
			continue;

		int id = stoi(fields[0]);

		if (id > maxId)
			maxId = id;

		Answer answerToAdd(stoi(fields[0]), stoi(fields[1]), stoi(fields[2]), fields[4], fields[3]);

		this->addAnswer(answerToAdd);
	}

	inputFile.close();

	this->currentId = maxId + 1;
}

int AnswerRepository::findAnswer(int id)
{
	auto position = find_if(
		this->answersDatabase.begin(),
		this->answersDatabase.end(),
		[id](Answer currentQuestion)
		{
			return currentQuestion.getId() == id;
		});

	if (position == this->answersDatabase.end())
		return -1;

	return position - this->answersDatabase.begin();
}

void AnswerRepository::addAnswer(Answer answerToAdd)
{
	if (this->findAnswer(answerToAdd.getId()) != -1)
		throw std::exception{ "Answer already in repository!" };

	this->answersDatabase.push_back(answerToAdd);
	this->currentId++;
}

vector<Answer>& AnswerRepository::getAll()
{
	return this->answersDatabase;
}

int AnswerRepository::getCurrentId()
{
	return this->currentId;
}

Answer& AnswerRepository::getAnswerById(int id)
{
	for (auto& answer : this->answersDatabase)
		if (answer.getId() == id)
			return answer;

	return answersDatabase[0];
}
