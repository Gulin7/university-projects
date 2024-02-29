#include "IdeasTableModel.h"

int IdeasTableModel::rowCount(const QModelIndex& parent) const
{
    return this->controller.getAllIdeas().size();
}

int IdeasTableModel::columnCount(const QModelIndex& parent) const
{
    return 5;
}

QVariant IdeasTableModel::data(const QModelIndex& index, int role) const
{
    int row = index.row();
    int column = index.column();
    Idea currentIdea = this->controller.getAllIdeas()[row];
    if(role == Qt::DisplayRole)
        switch (column) {
        case 0:
            return QString::fromStdString(currentIdea.getTitle());
        case 1:
            return QString::fromStdString(currentIdea.getDescription());
        case 2:
            return QString::fromStdString(currentIdea.getStatus());
        case 3:
            return QString::fromStdString(currentIdea.getCreator());
        case 4:
            return QString::fromStdString(std::to_string(currentIdea.getDuration()));
        default:
            break;
        }
    return QVariant();
}

QVariant IdeasTableModel::headerData(int section, Qt::Orientation orientation, int role) const
{
    if(role == Qt::DisplayRole)
        if(orientation == Qt::Horizontal)
            switch (section) {
            case 0:
                return QString("Title");
            case 1:
                return QString("Description");
            case 2:
                return QString("Status");
            case 3:
                return QString("Creator");
            case 4:
                return QString("Duration");
            default:
                break;
            }
    return QVariant();
}

void IdeasTableModel::addIdea(Idea& idea)
{
}

void IdeasTableModel::reviseIdea(int indexOfIdea)
{
}

std::vector<Idea> IdeasTableModel::acceptedIdeas(Researcher res)
{
    return std::vector<Idea>();
}
