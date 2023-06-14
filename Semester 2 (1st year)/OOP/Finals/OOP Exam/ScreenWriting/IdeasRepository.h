#pragma once

#include <vector>

#include "Idea.h"

using std::vector;

class IdeasRepository
{
private:
	vector<Idea> ideas;
	string filePath;

public:
	IdeasRepository(string filePath);

	void readFile();

	int findPosition(string description);
	Idea& getIdeaAtPosition(int position);
	Idea& getIdeaByDescription(string description);

	void add(Idea ideaToAdd);

	vector<Idea>& getAll();
};

