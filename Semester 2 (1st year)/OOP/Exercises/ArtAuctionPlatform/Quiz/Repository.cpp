#include "Repository.h"

void Repository::readFromFileParticipant()
{
	std::ifstream inputFile("participants.txt");
	std::string line;
	while (std::getline(inputFile, line)) {
		string token;
		vector<string> data;
		std::stringstream ss(line);
		while (std::getline(ss, token, ';')) {
			data.push_back(token);
		}
		Participant participant{ data[0], stoi(data[1]) };
		participants.push_back(participant);
	}
	inputFile.close();
}

void Repository::readFromFileQuestion()
{
	std::ifstream inputFile("questions.txt");
	std::string line;
	while (std::getline(inputFile, line)) {
		string token;
		vector<string> data;
		std::stringstream ss(line);
		while (std::getline(ss, token, ';')) {
			data.push_back(token);
		}
		Question question{ stoi(data[0]),data[1],data[2], stoi(data[3]) };
		questions.push_back(question);
	}
	inputFile.close();
}

void Repository::saveToFileQuestion()
{
	std::ofstream outputFile("questions.txt");
	for (auto& quest : this->questions) {
			outputFile << quest.toStringFile() << "\n";
	}
	outputFile.close();
}
