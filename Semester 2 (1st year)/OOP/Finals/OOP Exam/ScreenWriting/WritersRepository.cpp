#include "WritersRepository.h"

#include <fstream>

WritersRepository::WritersRepository(string filePath)
	: filePath{ filePath }
{
	this->readFile();
}

void WritersRepository::readFile()
{
	std::ifstream inputFile{ this->filePath };

	if (!inputFile.is_open())
		throw std::exception{ "Cannot open file for reading!" };

	string currentUser;

	while (getline(inputFile, currentUser))
	{
		vector<string> fields = splitString(currentUser, '|');

		if (fields.size() != 2)
			continue;

		ScreenWriter writerToAdd{ fields[0], fields[1] };

		this->add(writerToAdd);
	}
}

int WritersRepository::findPosition(string name)
{
	auto position = find_if(writers.begin(), writers.end(),
		[&name](ScreenWriter currentWriter)
		{
			return currentWriter.getName() == name;
		});

	if (position == writers.end())
		return -1;

	return position - writers.begin();
}

ScreenWriter& WritersRepository::getWriterAtPosition(int position)
{
	if (position < 0 || position >= writers.size())
		throw std::exception{ "Index out of range - repo!" };

	return this->writers[position];
}

ScreenWriter& WritersRepository::getWriterByName(string name)
{
	auto position = find_if(writers.begin(), writers.end(),
		[&name](ScreenWriter currentWriter)
		{
			return currentWriter.getName() == name;
		});

	if (position == writers.end())
		throw std::exception{ "Writer not in repository!" };

	return *position;
}

void WritersRepository::add(ScreenWriter writerToAdd)
{
	if (this->findPosition(writerToAdd.getName()) != -1)
		throw std::exception{ "Writer already in repo!" };

	this->writers.push_back(writerToAdd);
}

vector<ScreenWriter>& WritersRepository::getAll()
{
	return this->writers;
}
