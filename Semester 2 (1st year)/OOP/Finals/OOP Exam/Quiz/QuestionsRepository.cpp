#include "QuestionsRepository.h"
#include "StringOperations.h"

#include <exception>
#include <fstream>

QuestionsRepository::QuestionsRepository(const string& filePath) : filePath{ filePath }
{
	this->readFile();
}

void QuestionsRepository::readFile()
{
	std::ifstream inputFile{ this->filePath };

	if (!inputFile.is_open())
		throw std::exception{ "Cannot open questions file!" };

	string currentLine;

	while (std::getline(inputFile, currentLine))
	{
		vector<string> fields = splitString(currentLine, '|');

		if (fields.size() != 4)
			continue;

		Question currentQuestion{ stoi(fields[0]), fields[1], fields[2], stoi(fields[3])};

		this->add(currentQuestion);
	}

	inputFile.close();
}

void QuestionsRepository::writeFile()
{
	std::ofstream outputFile{ this->filePath };

	if (!outputFile.is_open())
		throw std::exception{ "Cannot open the file to write!" };

	for (auto question : this->questions)
		outputFile << question.toString() << "\n";

	outputFile.close();
}

Question& QuestionsRepository::getQuestionAtPosition(int position)
{
	if (position < 0 || position >= this->questions.size())
		throw std::exception{ "Index out of range!" };

	return this->questions[position];
}

int QuestionsRepository::findById(int id)
{
	auto position = std::find_if(this->questions.begin(), this->questions.end(),
		[&id](Question currentQuestion)
		{
			return currentQuestion.getId() == id;
		});

	if (position == this->questions.end())
		return -1;

	return position - this->questions.begin();
}

void QuestionsRepository::add(Question questionToAdd)
{
	if (this->findById(questionToAdd.getId()) != -1)
		throw std::exception{ "Question with this id already exists!" };

	this->questions.push_back(questionToAdd);
	this->writeFile();
}

vector<Question>& QuestionsRepository::getAll()
{
	return this->questions;
}
