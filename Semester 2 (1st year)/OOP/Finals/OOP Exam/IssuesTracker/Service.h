#pragma once

#include "IssueRepository.h"
#include "UserRepository.h"

#include <QAbstractTableModel>

class Service : public QAbstractTableModel
{
private:
	UserRepository& usersRepo;
	IssueRepository& issuesRepo;

public:
	Service(UserRepository& users, IssueRepository& issues);

	void addIssue(string description, string status, string reporter, string solver);
	void removeIssue(int issueIndex);

	Issue& getIssueAtPosition(int position);

	void resolveIssue(QModelIndex& index, string userName);

	User& getUserByName(string name);

	int rowCount(const QModelIndex& parent = QModelIndex()) const;
	int columnCount(const QModelIndex& parent = QModelIndex()) const;
	QVariant data(const QModelIndex& index, int role = Qt::DisplayRole) const;
	QVariant headerData(int section, Qt::Orientation orientation, int role = Qt::DisplayRole) const;
	Qt::ItemFlags flags(const QModelIndex& index) const;
};

