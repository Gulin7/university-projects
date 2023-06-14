#pragma once

#include <vector>

#include "ScreenWriter.h"
#include "StringOperations.h"

using std::vector;

class WritersRepository
{
private:
	vector<ScreenWriter> writers;
	string filePath;

public:
	WritersRepository(string filePath);

	void readFile();

	int findPosition(string name);
	ScreenWriter& getWriterAtPosition(int position);
	ScreenWriter& getWriterByName(string name);

	void add(ScreenWriter writerToAdd);

	vector<ScreenWriter>& getAll();
};

