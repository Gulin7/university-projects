#include "IssueRepository.h"
#include "StringOperations.h"

#include <fstream>
#include <algorithm>

IssueRepository::IssueRepository(string filePath) : filePath { filePath }
{
	this->readFile();
}

void IssueRepository::readFile()
{
	std::ifstream inputFile{ this->filePath };

	if (!inputFile.is_open())
		throw std::exception{ "Cannot open file to read!" };

	string currentIssue;

	while (getline(inputFile, currentIssue))
	{
		vector<string> fields = splitString(currentIssue, '|');

		if (fields.size() != 4)
			continue;

		Issue issueToAdd{ fields[0], fields[1], fields[2], fields[3] };
		this->add(issueToAdd);
	}

	inputFile.close();
}

void IssueRepository::saveFile()
{
	std::ofstream outputFile{ this->filePath };

	if (!outputFile.is_open())
		throw std::exception{ "Cannot open file to write!" };

	for (auto user : this->getAll())
		outputFile << user.toString() << "\n";

	outputFile.close();
}

int IssueRepository::findPosition(string issueDescription)
{
	auto position = std::find_if(issues.begin(), issues.end(),
		[&issueDescription](Issue currentIssue)
		{
			return currentIssue.getDescription() == issueDescription;
		});

	if (position == issues.end()) return -1;

	return position - issues.begin();
}

Issue& IssueRepository::getIssueAtPosition(int position)
{
	if (position < 0 || position >= issues.size())
		throw std::runtime_error{ "Index out of range!" };

	return issues[position];
}

void IssueRepository::add(Issue issueToAdd)
{
	if (this->findPosition(issueToAdd.getDescription()) != -1)
		throw std::exception{ "Issue already in repository!" };

	this->issues.push_back(issueToAdd);

	sort(this->issues.begin(), this->issues.end(),
		[](Issue firstIssue, Issue secondIssue)
		{
			if (firstIssue.getStatus() == secondIssue.getStatus())
				return firstIssue.getDescription() < secondIssue.getDescription();

			return firstIssue.getStatus() < secondIssue.getStatus();
		});
}

void IssueRepository::remove(string issueDescription)
{
	int position = this->findPosition(issueDescription);

	if (position == -1)
		throw std::exception{ "Issue not in repo!" };

	this->issues.erase(this->issues.begin() + position);

	sort(this->issues.begin(), this->issues.end(),
		[](Issue firstIssue, Issue secondIssue)
		{
			if (firstIssue.getStatus() == secondIssue.getStatus())
				return firstIssue.getDescription() < secondIssue.getDescription();

			return firstIssue.getStatus() < secondIssue.getStatus();
		});
}

vector<Issue>& IssueRepository::getAll()
{
	return this->issues;
}

IssueRepository::~IssueRepository()
{
	this->saveFile();
}
