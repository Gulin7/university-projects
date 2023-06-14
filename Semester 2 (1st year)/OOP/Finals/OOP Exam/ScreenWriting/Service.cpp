#include "Service.h"


Service::Service(WritersRepository& writers, IdeasRepository& ideas) :
    writersRepo{ writers }, ideasRepo{ ideas }
{
}

void Service::addIdea(string description, string status, string creator, int act)
{
    this->beginInsertRows(QModelIndex(), this->rowCount(), this->rowCount());

    if (description == "")
        throw std::exception{ "Description cannot be empty!" };

    if (act < 1 || act > 3)
        throw std::exception{ "Act must be between 1 and 3!" };

    Idea ideaToAdd{ description, status, creator, act };
    this->ideasRepo.add(ideaToAdd);

    this->endInsertRows();
}

ScreenWriter& Service::getWriterByName(string name)
{
    return this->writersRepo.getWriterByName(name);
}

Idea& Service::getIdeaByDescription(string description)
{
    return this->ideasRepo.getIdeaByDescription(description);
}

void Service::reviseIdea(QModelIndex& position, string description)
{
    Idea& requiredIdea = this->ideasRepo.getIdeaByDescription(description);
    requiredIdea.setStatus("accepted");

    emit dataChanged(position, position);
}

int Service::rowCount(const QModelIndex& parent) const
{
    return this->ideasRepo.getAll().size();
}

int Service::columnCount(const QModelIndex& parent) const
{
    return 4;
}

QVariant Service::data(const QModelIndex& index, int role) const
{
    int row = index.row();
    int column = index.column();

    Idea& requiredIdea = this->ideasRepo.getIdeaAtPosition(row);

    if (role == Qt::EditRole || role == Qt::DisplayRole)
    {
        switch (column)
        {
        case 0:
            return QString::fromStdString(requiredIdea.getDescription());
            
        case 1:
            return QString::fromStdString(requiredIdea.getStatus());

        case 2:
            return QString::fromStdString(requiredIdea.getCreator());

        case 3:
            return QString::number(requiredIdea.getAct());
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
            return "Creator";

        case 3:
            return "Act";
        }
    }

    return QVariant();
}
