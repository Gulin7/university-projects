#include "writerWindow.h"

#include <QMessageBox>

writerWindow::writerWindow(QAbstractItemModel* model, Service& service, string writerName, QWidget* parent)
    : QWidget(parent), service{ service }, writerName{ writerName }
{
    ui.setupUi(this);

    ui.ideasTable->setModel(model);
    this->setWindowTitle(QString::fromStdString(writerName));

    ScreenWriter currentWriter = this->service.getWriterByName(writerName);

    if (currentWriter.getExpertise() != "Senior")
        ui.reviseIdeaButton->hide();

    connectSignals();
}


void writerWindow::addIdea()
{
    string description = ui.descriptionInput->text().toStdString();
    int act = ui.actInput->text().toInt();

    try
    {
        this->service.addIdea(description, "proposed", this->writerName, act);
    }
    catch (std::exception& e)
    {
        QMessageBox alert;

        alert.setText(e.what());
        alert.exec();
    }
}

void writerWindow::connectSignals()
{
    connect(ui.addIdeaButton, &QPushButton::clicked, this, &writerWindow::addIdea);
    connect(ui.ideasTable, &QTableView::clicked, this, &writerWindow::checkForDisableReviseButton);
    connect(ui.reviseIdeaButton, &QPushButton::clicked, this, &writerWindow::reviseIdea);
}

void writerWindow::checkForDisableReviseButton()
{
    QModelIndex position = ui.ideasTable->selectionModel()->selectedIndexes().at(0);

    QModelIndex descriptionPosition = ui.ideasTable->model()->index(position.row(), 0);
    QVariant data = ui.ideasTable->model()->data(descriptionPosition);

    Idea requiredIdea = this->service.getIdeaByDescription(data.toString().toStdString());

    if (requiredIdea.getStatus() == "proposed")
        ui.reviseIdeaButton->setEnabled(true);

    else
        ui.reviseIdeaButton->setDisabled(true);
}

void writerWindow::reviseIdea()
{
    if (ui.ideasTable->selectionModel()->selectedIndexes().size() != 1)
    {
        QMessageBox alert;
        alert.setText("Please select an idea!");
        alert.exec();
    }

    QModelIndex position = ui.ideasTable->selectionModel()->selectedIndexes().at(0);
    QModelIndex revisedPosition = ui.ideasTable->model()->index(position.row(), 1);

    QModelIndex descriptionPosition = ui.ideasTable->model()->index(position.row(), 0);
    QVariant data = ui.ideasTable->model()->data(descriptionPosition);

    this->service.reviseIdea(revisedPosition, data.toString().toStdString());
}


writerWindow::~writerWindow()
{}