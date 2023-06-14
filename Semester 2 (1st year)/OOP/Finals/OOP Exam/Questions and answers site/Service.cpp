#include "Service.h"

#include <unordered_map>
#include <algorithm>
#include <iterator>

using std::unordered_map;

int Service::computeMatches(string firstText, string secondText)
{
	int count = 0;

	for (int i = 0; i < firstText.size() && i < secondText.size(); i++)
		if (firstText[i] == secondText[i])
			count++;
	
	return count;
}

Service::Service(UserRepository& userRepo, QuestionsRepository& questionsRepo, AnswerRepository& answerRepo) :
	userRepo{ userRepo }, questionsRepo{ questionsRepo }, answerRepo{ answerRepo }
{
}

vector<Question> Service::getQuestionsSortedByAnswers()
{
	vector<Question> allQuestion{ this->questionsRepo.getAll() };
	unordered_map<int, int> frequency;

	for (auto& question : allQuestion)
		frequency[question.getId()] = 0;

	vector<Answer> allAnswers{ this->answerRepo.getAll() };

	for (auto& answer : allAnswers)
		frequency[answer.getQuestionId()]++;


	std::sort(allQuestion.begin(), allQuestion.end(),
		[&frequency](Question q1, Question q2)
		{
			return frequency[q1.getId()] > frequency[q2.getId()];
		});

	return allQuestion;
}

Question Service::getMatchedQuestion(string text)
{
	int bestMatch = 0;
	Question matchedQuestion;

	for (auto question : this->questionsRepo.getAll())
	{
		int currentMatch = this->computeMatches(question.getText(), text);

		if (currentMatch > bestMatch)
		{
			bestMatch = currentMatch;
			matchedQuestion = question;
		}
	}

	return matchedQuestion;
}

vector<Answer> Service::getAnswers(int questionId)
{
	vector<Answer> result, allAnswers = this->answerRepo.getAll();

	std::copy_if(allAnswers.begin(), allAnswers.end(), std::back_inserter(result),
		[&questionId](Answer currentAnswer)
		{
			return currentAnswer.getQuestionId() == questionId;
		});

	sort(result.begin(), result.end(),
		[](Answer firstAnswer, Answer secondAnswer)
		{
			return firstAnswer.getNumberOfVotes() > secondAnswer.getNumberOfVotes();
		});

	return result;
}

void Service::addQuestion(string userName, string text)
{
	if (text == "")
		throw std::exception{ "Description cannot be empty!" };

	int questionId = this->questionsRepo.getCurrentId();

	Question questionToAdd{ questionId, text, userName };

	this->questionsRepo.addQuestion(questionToAdd);

	this->notify();
}

int Service::getQuestionId(string questionText)
{
	return this->questionsRepo.findByDescription(questionText);
}

void Service::addAnswer(string userName, string text, int questionId)
{
	if (text == "")
		throw std::exception{ "Description cannot be empty!" };

	int answerId = this->answerRepo.getCurrentId();

	Answer answerToAdd{ answerId, questionId, 0, userName, text };
	this->answerRepo.addAnswer(answerToAdd);

	this->notify();
}

void Service::updateAnswerNumberOfVotes(int answerId, int newNumberOfVotes)
{
	Answer& answerToUpdate = this->answerRepo.getAnswerById(answerId);

	answerToUpdate.setNumberOfVotes(newNumberOfVotes);

	this->notify();
}

