#include "IdeasRepository.h"
#include "StringOperations.h"

#include <fstream>
#include <algorithm>

IdeasRepository::IdeasRepository(string filePath) : filePath{ filePath }
{
	this->readFile();
}

void IdeasRepository::readFile()
{
	std::ifstream inputFile{ this->filePath };

	if (!inputFile.is_open())
		throw std::exception{ "Cannot open file for read!" };

	string currentIdea;

	while (getline(inputFile, currentIdea))
	{
		vector<string> fields = splitString(currentIdea, '|');

		if (fields.size() != 4)
			continue;

		Idea ideaToAdd{ fields[0], fields[1], fields[2], stoi(fields[3]) };

		this->add(ideaToAdd);
	}
}

int IdeasRepository::findPosition(string description)
{
	auto position = find_if(ideas.begin(), ideas.end(),
		[&description](Idea currentIdea)
		{
			return currentIdea.getDescription() == description;
		});

	if (position == ideas.end())
		return -1;

	return position - ideas.begin();
}

Idea& IdeasRepository::getIdeaAtPosition(int position)
{
	if (position < 0 || position >= ideas.size())
		throw std::exception{ "Index out of range - ideas repo!" };

	return ideas[position];
}

Idea& IdeasRepository::getIdeaByDescription(string description)
{
	auto position = find_if(ideas.begin(), ideas.end(),
		[&description](Idea currentIdea)
		{
			return currentIdea.getDescription() == description;
		});

	if (position == ideas.end())
		throw std::exception{ "Idea not in repo!" };

	int index = position - ideas.begin();

	return ideas[index];
}

void IdeasRepository::add(Idea ideaToAdd)
{
	if (this->findPosition(ideaToAdd.getDescription()) != -1)
		throw std::exception{ "Idea already in repo!" };

	this->ideas.push_back(ideaToAdd);

	sort(ideas.begin(), ideas.end(),
		[](Idea firstIdea, Idea secondIdea)
		{
			return firstIdea.getAct() < secondIdea.getAct();
		});
}

vector<Idea>& IdeasRepository::getAll()
{
	return this->ideas;
}
