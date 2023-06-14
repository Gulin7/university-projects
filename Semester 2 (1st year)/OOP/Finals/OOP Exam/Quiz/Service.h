#pragma once

#include "ParticipantsRepository.h"
#include "QuestionsRepository.h"

#include "Subject.h"

#include <QAbstractListModel>

class Service : public QAbstractListModel
{
	Q_OBJECT

private:
	ParticipantsRepository& participants;
	QuestionsRepository& questions;

public:
	Service(ParticipantsRepository& participants, QuestionsRepository& questions);

	vector<Question> getAllQuestionsSortedById();
	vector<Question> getAllQuestionsSortedByScore();

	Question getQuestionById(int id);

	void addQuestion(int questionId, string questionText, string questionAnswer, int questionScore);
	void updateParticipantScore(string participantName, int newScore);

	// methods for model
	int rowCount(const QModelIndex& parent = QModelIndex()) const;
	int columnCount(const QModelIndex& parent) const;
	QVariant headerData(int section, Qt::Orientation orientation, int role = Qt::DisplayRole) const;
	QVariant data(const QModelIndex& index, int role = Qt::DisplayRole) const;
	bool setData(const QModelIndex& index, const QVariant& value, int role);

	Qt::ItemFlags flags(const QModelIndex& index) const;

signals:
	void dataChangedSignal();

};


