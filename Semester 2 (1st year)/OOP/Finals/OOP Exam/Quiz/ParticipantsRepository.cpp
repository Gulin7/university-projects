#include "ParticipantsRepository.h"

#include <exception>
#include <fstream>

ParticipantsRepository::ParticipantsRepository(const string& filePath) : filePath{ filePath }
{
	this->readFile();
}

void ParticipantsRepository::readFile()
{
	std::ifstream inputFile{ this->filePath };

	if (!inputFile.is_open())
		throw std::exception{ "Cannot open participants file!" };

	string currentParticipantName;

	while (std::getline(inputFile, currentParticipantName))
	{
		Participant currentParticipant{ currentParticipantName };
		this->add(currentParticipant);
	}

	inputFile.close();
}

Participant& ParticipantsRepository::getParticipantAtPosition(int position)
{
	if (position < 0 || position >= this->participants.size())
		throw std::exception{ "Position not in repository!" };

	return participants[position];
}

int ParticipantsRepository::findByName(const string& name)
{
	auto position = std::find_if(this->participants.begin(), this->participants.end(),
		[&name](Participant currentParticipant)
		{
			return currentParticipant.getName() == name;
		});

	if (position == this->participants.end())
		return -1;

	return position - this->participants.begin();
}

void ParticipantsRepository::add(Participant participantToAdd)
{
	if (this->findByName(participantToAdd.getName()) != -1)
		throw std::exception{ "Participant already exists!" };

	this->participants.push_back(participantToAdd);
}

vector<Participant>& ParticipantsRepository::getAll()
{
	return this->participants;
}
