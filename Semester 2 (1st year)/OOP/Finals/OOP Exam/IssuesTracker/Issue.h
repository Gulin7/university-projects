#pragma once

#include <string>

using std::string;

class Issue
{
private:
	string description, status, reporter, solver;

public:
	Issue(string description, string status, string reporter, string solver);

	string getDescription();
	string getStatus();
	string getReporter();
	string getSolver();

	string toString();

	void setSolver(string newSolver);
	void setStatus(string newStatus);
};

