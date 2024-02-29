#include "Controller.h"

void Controller::readIdeasFromFile()
{
	std::ifstream inputFile(this->ideasFile);
	string line;
	while (std::getline(inputFile, line)) {
		string token;
		vector<string>data;
		std::stringstream ss(line);
		while (std::getline(ss, token, ';')) {
			data.push_back(token);
		}
		Idea idea(data[0], data[1],data[2],data[3],stoi(data[4]));
		this->addIdea(idea);
	}
	inputFile.close();
}

void Controller::readResearchersFromFile()
{
	std::ifstream inputFile(this->ideasFile);
	string line;
	while (std::getline(inputFile, line)) {
		string token;
		vector<string>data;
		std::stringstream ss(line);
		while (std::getline(ss, token, ';')) {
			data.push_back(token);
		}
		Researcher res(data[0], data[1]);
		this->addResearcher(res);
	}
	inputFile.close();
}

void Controller::saveIdeasToFile()
{
	std::ofstream outputFile(this->ideasFile);
	for (auto& idea : this->ideas) {
		outputFile << idea.toStringFile() << '\n';
	}
	outputFile.close();
}
