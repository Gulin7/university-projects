#pragma once
#include <vector>
#include <string>

using std::string;
using std::vector;

class Question
{
private:
	string text, answer;
	int id, score;
public:
	Question(int id, string text, string answer, int score): id(id), text(text), answer(answer), score(score){}

	string toString();
	
	int getId() { return id; }
	string getText() { return text; }
	string getAnswer() { return answer; }
	int getScore() { return score; }

	string toStringNoAnswer();
	string toStringFile();

	void operator=(Question& newQ) {
		this->id = newQ.getId();
		this->text = newQ.getText();
		this->answer = newQ.getAnswer();
		this-> score = newQ.getScore();
	}

	~Question(){}
};

