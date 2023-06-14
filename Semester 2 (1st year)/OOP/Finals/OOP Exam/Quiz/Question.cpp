#include "Question.h"

Question::Question(int id, string text, string correctAnswer, int score) :
	id{ id }, score{ score }, text{ text }, correctAnswer{ correctAnswer }
{
}

int Question::getId()
{
	return this->id;
}

int Question::getScore()
{
	return this->score;
}

string Question::getText()
{
	return this->text;
}

string Question::getCorrectAnswer()
{
	return this->correctAnswer;
}

string Question::toString()
{
	return std::to_string(this->id) + " | " + this->text + " | " + this->correctAnswer + " | " + std::to_string(this->score);
}
