#pragma once

#include "UserRepository.h"
#include "QuestionsRepository.h"
#include "AnswerRepository.h"

#include "Subject.h"

class Service : public Subject
{
private:
	UserRepository& userRepo;
	QuestionsRepository& questionsRepo;
	AnswerRepository& answerRepo;

	int computeMatches(string firstText, string secondText);

public:
	Service(UserRepository& userRepo, QuestionsRepository& questionsRepo, AnswerRepository& answerRepo);

	vector<Question> getQuestionsSortedByAnswers();
	Question getMatchedQuestion(string text);

	vector<Answer> getAnswers(int questionId);
	void addQuestion(string userName, string text);
	int getQuestionId(string questionText);

	void addAnswer(string userName, string text, int questionId);
	void updateAnswerNumberOfVotes(int answerId, int newNumberOfVotes);
};

