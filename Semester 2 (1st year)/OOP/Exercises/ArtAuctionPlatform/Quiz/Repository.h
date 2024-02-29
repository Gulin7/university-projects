#pragma once
#include "Question.h"
#include "Participant.h"
#include <fstream>
#include <sstream>
#include <exception>
#include <algorithm>
#include "Subject.h"

class Repository:
	public Subject
{
private:
	vector<Question> questions;
	vector<Participant> participants;
public:
	Repository() { this->readFromFileParticipant(); this->readFromFileQuestion(); }

	void readFromFileParticipant();
	void readFromFileQuestion();
	void saveToFileQuestion();

	vector<Question> getAllQuestions() { return this->questions; }
	vector<Participant> getAllParticipants() { return this->participants; }

	int findQuestionById(int id) {
		for (int i = 0; i < this->questions.size(); i++) {
			if (this->questions[i].getId() == id) {
				return i;
			}
		}
		return -1;
	}

	void increasePartScore(string name, int score) {
		for (int i = 0; i < participants.size(); i++)
			if (participants[i].getName() == name){
				participants[i].setScore(participants[i].getScore() + score);
			break;
			}
	}
	Participant findParticipantByName(string name) {
		for (auto& part : participants)
			if (name == part.getName())
				return part;
	}

	void addQuestion(Question quest) {
		int position = this->findQuestionById(quest.getId());
		if(position!=-1)
			throw std::exception("Question already exists!");
		this->questions.push_back(quest);
	}

	~Repository() { this->saveToFileQuestion(); }
};

