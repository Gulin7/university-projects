#pragma once

#include <vector>

#include "Issue.h"

using std::vector;

class IssueRepository
{
private:
	vector<Issue> issues;

	string filePath;

public:
	IssueRepository(string filePath);

	void readFile();
	void saveFile();

	int findPosition(string issueDescription);

	Issue& getIssueAtPosition(int position);
	void add(Issue issueToAdd);
	void remove(string issueDescription);

	vector<Issue>& getAll();

	~IssueRepository();
};

