#include "Service.h"

#include <algorithm>

Service::Service(ParticipantsRepository& participants, QuestionsRepository& questions) :
	participants{ participants }, questions{ questions }
{
}

vector<Question> Service::getAllQuestionsSortedById()
{
	vector<Question> allQuestions = this->questions.getAll();

	std::sort(allQuestions.begin(), allQuestions.end(),
		[](Question firstQuestion, Question secondQuestion)
		{
			return firstQuestion.getId() < secondQuestion.getId();
		});

	return allQuestions;
}

vector<Question> Service::getAllQuestionsSortedByScore()
{
	vector<Question> allQuestions = this->questions.getAll();

	std::sort(allQuestions.begin(), allQuestions.end(),
		[](Question firstQuestion, Question secondQuestion)
		{
			return firstQuestion.getScore() > secondQuestion.getScore();
		});

	return allQuestions;
}

Question Service::getQuestionById(int id)
{
	int position = this->questions.findById(id);
	return this->questions.getQuestionAtPosition(position);
}

void Service::addQuestion(int questionId, string questionText, string questionAnswer, int questionScore)
{
	/*
	* Function to add a question to the repository
	* <param> questionId -> integer, representing the id of the question
	* <param> questionText -> string, representing the question
	* <param> questionAnswer -> string, representing the answer of the question
	* <param> questionScore -> int, representing the score of the question in case of correct answer
	* 
	* <return> None
	*/

	Question questionToAdd{ questionId, questionText, questionAnswer, questionScore };

	this->questions.add(questionToAdd);

	emit dataChangedSignal();
}

void Service::updateParticipantScore(string participantName, int newScore)
{
	/*
	* Function to update the score of a given participant
	* <param> participantName -> string, the name of the participant for which we want to update the score
	* <param> newScore -> int, new score for the given participant
	*/
	int position = this->participants.findByName(participantName);

	Participant& requiredParticipant = this->participants.getParticipantAtPosition(position);
	requiredParticipant.setScore(newScore);
}

int Service::rowCount(const QModelIndex& parent) const
{
	return questions.getAll().size();
}

int Service::columnCount(const QModelIndex& parent) const
{
	return 4;
}

QVariant Service::headerData(int section, Qt::Orientation orientation, int role) const
{
	if (role == Qt::DisplayRole && orientation == Qt::Horizontal)
	{
		switch (section)
		{
		case 0:
			return "Id";
		case 1:
			return "Text";
		case 2:
			return "Answer";
		case 3:
			return "Score";
		}
	}

	return QVariant();
}

QVariant Service::data(const QModelIndex& index, int role) const
{
	int row = index.row();
	int column = index.column();

	Question requiredQuestion = this->questions.getAll()[row];

	if (role == Qt::DisplayRole || role == Qt::EditRole)
	{
		return QString::fromStdString(requiredQuestion.toString());
	}

	return QVariant();
}

bool Service::setData(const QModelIndex& index, const QVariant& value, int role)
{
	return false;
}

Qt::ItemFlags Service::flags(const QModelIndex& index) const
{
	return Qt::ItemIsEditable | Qt::ItemIsSelectable | Qt::ItemIsEnabled | QAbstractListModel::flags(index);
}

