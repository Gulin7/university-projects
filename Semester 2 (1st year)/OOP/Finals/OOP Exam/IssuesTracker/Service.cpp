#include "Service.h"

Service::Service(UserRepository& users, IssueRepository& issues) :
	usersRepo { users }, issuesRepo { issues }
{
}

void Service::addIssue(string description, string status, string reporter, string solver)
{
	beginInsertRows(QModelIndex(), this->rowCount(), this->rowCount());

	Issue issueToAdd{ description, status, reporter, solver };
	this->issuesRepo.add(issueToAdd);

	endInsertRows();
}

void Service::removeIssue(int issueIndex)
{
	beginRemoveRows(QModelIndex(), issueIndex, issueIndex);

	Issue requiredIssue = this->issuesRepo.getIssueAtPosition(issueIndex);
	string description = requiredIssue.getDescription();

	if (requiredIssue.getStatus() != "closed")
		throw std::exception{ "Issue is open!" };

	this->issuesRepo.remove(description);

	endRemoveRows();
}

Issue& Service::getIssueAtPosition(int position)
{
	return this->issuesRepo.getIssueAtPosition(position);
}

void Service::resolveIssue(QModelIndex& index, string userName)
{
	int row = index.row();

	Issue& requiredIssue = this->getIssueAtPosition(row);

	requiredIssue.setSolver(userName);
	requiredIssue.setStatus("closed");

	QModelIndex leftIndex = this->index(row, 1);
	QModelIndex rightIndex = this->index(row, 3);

	emit dataChanged(leftIndex, rightIndex);
}

User& Service::getUserByName(string name)
{
	int position = this->usersRepo.findPosition(name);
	User& requiredUser = this->usersRepo.getUserAtPosition(position);

	return requiredUser;
}

int Service::rowCount(const QModelIndex& parent) const
{
	return issuesRepo.getAll().size();
}

int Service::columnCount(const QModelIndex& parent) const
{
	return 4;
}

QVariant Service::data(const QModelIndex& index, int role) const
{
	int row = index.row();
	int column = index.column();

	Issue currentIssue = this->issuesRepo.getAll()[row];

	if (role == Qt::EditRole || role == Qt::DisplayRole)
	{
		switch (column)
		{
		case 0:
			return QString::fromStdString(currentIssue.getDescription());

		case 1:
			return QString::fromStdString(currentIssue.getStatus());

		case 2:
			return QString::fromStdString(currentIssue.getReporter());

		case 3:
			return QString::fromStdString(currentIssue.getSolver());
		}
	}

	return QVariant();
}

QVariant Service::headerData(int section, Qt::Orientation orientation, int role) const
{
	if (orientation == Qt::Horizontal && role == Qt::DisplayRole)
	{
		switch (section)
		{
		case 0:
			return "Description";

		case 1:
			return "Status";
			
		case 2:
			return "Reporter";

		case 3:
			return "Solver";
		}
	}

	return QVariant();
}

Qt::ItemFlags Service::flags(const QModelIndex& index) const
{
	return Qt::ItemIsEditable | Qt::ItemIsEnabled | Qt::ItemIsSelectable | Qt::ItemFlags();
}
