#pragma once

#include <vector>

#include "Participant.h"

using std::vector;

class ParticipantsRepository
{
private:
	vector<Participant> participants;
	string filePath;

public:
	ParticipantsRepository(const string& filePath);

	void readFile();

	Participant& getParticipantAtPosition(int position);
	int findByName(const string& name);
	void add(Participant participantToAdd);
	vector<Participant>& getAll();
};

