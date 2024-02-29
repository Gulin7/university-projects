#pragma once
#include <vector>
#include <string>

using std::string;
using std::vector;

class Participant
{
private:
	string name;
	int score;
public:
	Participant(string name, int score) : name(name), score(score) {}

	string getName() { return name; }
	int getScore() { return score; }

	void setScore(int score) { this->score = score; }

	~Participant() {}
};

