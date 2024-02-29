#pragma once
#include "Idea.h"
#include "Subject.h"
#include "Researcher.h"
#include <algorithm>

bool compareIdeas(Idea i1, Idea i2) {
	if (i1.getDuration() < i2.getDuration())
		return true;
	return false;
}

class Controller:
	public Subject
{
private:
	vector<Idea> ideas;
	vector<Researcher> researchers;
	string researchersFile;
	string ideasFile;

public:
	Controller(string researchersFile, string ideasFile): researchersFile(researchersFile), ideasFile(ideasFile) {
		this->readIdeasFromFile();
		this->readResearchersFromFile();
	}

	void readIdeasFromFile();
	void readResearchersFromFile();
	void saveIdeasToFile();

	void addIdea(Idea idea) {
		this->ideas.push_back(idea);
	}

	void addResearcher(Researcher res) {
		this->researchers.push_back(res);
	}

	vector<Idea> getAllIdeas() { 
		vector<Idea> allIdeas = ideas;
		std::sort(allIdeas.begin(), allIdeas.end(), compareIdeas);
		return allIdeas; }
	vector<Researcher> getAllResearchers() { return this->researchers; }

	int findResearcherPositionByName(string name) {
		auto position = std::find_if(researchers.begin(), researchers.end(), [&name](Researcher& res) { return name == res.getName();  });
		return position - researchers.begin();
	}

	Researcher getResearcherByName(string name) {
		return researchers[this->findResearcherPositionByName(name)];
	}

	vector<Idea> getAllIdeasByResearcherName(string name) {
		vector<Idea> ideasByResearcher;
		for (auto& idea : ideas) {
			if (idea.getCreator() == name)
				ideasByResearcher.push_back(idea);
		}
		return ideasByResearcher;
	}

	~Controller(){}
};

