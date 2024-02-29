#include "ResearcherWindow.h"

ResearcherWindow::ResearcherWindow(Controller& controller, string userName, QWidget *parent)
    : controller(controller), userName(userName), QMainWindow(parent)
{
    ui.setupUi(this);

    Researcher res = this->controller.getResearcherByName(userName);
    if (res.getPosition() == "senior")
        status = 1;
    else status = 0;

    this->populateList();
}

ResearcherWindow::~ResearcherWindow()
{}

void ResearcherWindow::update()
{
    this->populateList();
}

void ResearcherWindow::populateList()
{
}

void ResearcherWindow::develop() {

}

void ResearcherWindow::saveAll()
{
}

void ResearcherWindow::save()
{
}

void ResearcherWindow::addNewIdea()
{
}

void ResearcherWindow::acceptIdea()
{
}
