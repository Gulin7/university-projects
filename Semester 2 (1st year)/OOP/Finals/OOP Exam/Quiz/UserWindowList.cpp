#include "UserWindowList.h"

UserWindowList::UserWindowList(Service& service, QWidget *parent)
	: QWidget(parent), service { service }
{
	ui.setupUi(this);

	ui.questionsList->setModel(&service);
	connect(&service, &Service::dataChangedSignal, this, &UserWindowList::handleDataChange);
}

UserWindowList::~UserWindowList()
{}

void UserWindowList::handleDataChange()
{
	ui.questionsList->reset();
	ui.questionsList->update();
}
