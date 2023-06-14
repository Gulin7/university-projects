#pragma once

#include "WritersRepository.h"
#include "IdeasRepository.h"

#include <QAbstractTableModel>

class Service : public QAbstractTableModel
{
private:
	WritersRepository& writersRepo;
	IdeasRepository& ideasRepo;

public:
	Service(WritersRepository& writers, IdeasRepository& ideas);

	void addIdea(string description, string status, string creator, int act);

	ScreenWriter& getWriterByName(string name);
	Idea& getIdeaByDescription(string description);
	void reviseIdea(QModelIndex& position, string description);

	// model methods
	int rowCount(const QModelIndex& parent = QModelIndex()) const;
	int columnCount(const QModelIndex& parent = QModelIndex()) const;
	QVariant data(const QModelIndex& index, int role = Qt::DisplayRole) const;
	QVariant headerData(int section, Qt::Orientation orientation, int role = Qt::DisplayRole) const;
};

