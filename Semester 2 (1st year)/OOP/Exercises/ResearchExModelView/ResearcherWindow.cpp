#include "ResearcherWindow.h"
#include <QMessageBox>

ResearcherWindow::ResearcherWindow(IdeasTableModel* model, Researcher res, QWidget* parent)
    : model(model), researcher(res), QMainWindow(parent)
{
    ui.setupUi(this);

    ui.tableView->setModel(model);

    this->setWindowTitle(QString::fromStdString(researcher.getName()));
    if (researcher.getPosition() != "senior")
    {
        ui.acceptpushButton->hide();
        ui.saveAllpushButton->hide();
    }

    this->populateList();
}

ResearcherWindow::~ResearcherWindow()
{}

void ResearcherWindow::populateList()
{
}

void ResearcherWindow::develop() {

}

void ResearcherWindow::saveAll()
{
    this->model->controller.saveAcceptedIdeasToFile(); // only accepted
}

void ResearcherWindow::save()
{
    this->model->controller.saveIdeasToFile();
}

void ResearcherWindow::addNewIdea()
{
    string title = ui.titlelineEdit->text().toStdString();
    string description = ui.descriptionlineEdit->text().toStdString();
    int duration = ui.durationlineEdit->text().toInt();
    Idea idea{ title, description, duration, this->researcher.getName(), "proposed" };
    try {
        model->addIdea(idea);
    }
    catch (std::exception& e) {
        QMessageBox::warning(this, "Warning", e.what());
    }
}

void ResearcherWindow::acceptIdea()
{
    int index = ui.tableView->currentIndex().row();
    try {
        model->reviseIdea(index);
    }
    catch (std::exception& e) {
        QMessageBox::warning(this, "Warning", e.what());
    }
}
