#include "UserWindow.h"

#include <QMessageBox>

UserWindow::UserWindow(QAbstractItemModel* model, Service& service, string userName, QWidget *parent)
	: QWidget(parent), service{ service }, userName{ userName }
{
	ui.setupUi(this);
	ui.questionsTable->setModel(model);

	this->setWindowTitle(QString::fromStdString(userName));

	currentUser = this->service.getUserByName(this->userName);

	if (currentUser.getType() == "programmer")
	{
		ui.addIssueButton->setDisabled(true);
		ui.descriptionInput->setDisabled(true);
	}

	else
	{
		ui.resolveButton->setDisabled(true);
	}

	connect(ui.addIssueButton, &QPushButton::clicked, this, &UserWindow::addIssue);
	connect(ui.removeButton, &QPushButton::clicked, this, &UserWindow::removeIssue);
	connect(ui.questionsTable, &QAbstractItemView::clicked, this, &UserWindow::checkForDisableButton);
	connect(ui.resolveButton, &QPushButton::clicked, this, &UserWindow::resolveIssue);
}

UserWindow::~UserWindow()
{}

void UserWindow::addIssue()
{
	string description = ui.descriptionInput->text().toStdString();

	if (description == "")
	{
		QMessageBox alert;
		alert.setText("Please enter the description!");

		alert.exec();
	}

	try
	{
		this->service.addIssue(description, "open", this->userName, "-");
	}

	catch (std::exception& e)
	{
		QMessageBox alert;
		alert.setText(e.what());

		alert.exec();
	}
}

void UserWindow::removeIssue()
{
	if (ui.questionsTable->selectionModel()->selectedIndexes().size() != 1)
	{
		QMessageBox alert;
		alert.setText("Please select one issue!");

		alert.exec();

		return;
	}

	QModelIndex selectedIssue = ui.questionsTable->selectionModel()->selectedIndexes().at(0);
	int row = selectedIssue.row();

	try
	{
		this->service.removeIssue(row);
	}

	catch (std::exception& e)
	{
		QMessageBox alert;
		alert.setText(e.what());

		alert.exec();
	}
}

void UserWindow::checkForDisableButton()
{
	QModelIndex selectedIssue = ui.questionsTable->selectionModel()->selectedIndexes().at(0);
	int row = selectedIssue.row();

	Issue requiredIssue = this->service.getIssueAtPosition(row);

	if (requiredIssue.getStatus() == "closed")
		ui.resolveButton->setDisabled(true);

	else
		ui.resolveButton->setEnabled(true);

	if (currentUser.getType() == "programmer")
	{
		ui.addIssueButton->setDisabled(true);
		ui.descriptionInput->setDisabled(true);
	}

	else
	{
		ui.resolveButton->setDisabled(true);
	}
}

void UserWindow::resolveIssue()
{
	if (ui.questionsTable->selectionModel()->selectedIndexes().size() != 1)
	{
		QMessageBox alert;
		alert.setText("Please select one issue!");

		alert.exec();

		return;
	}

	QModelIndex selectedIssue = ui.questionsTable->selectionModel()->selectedIndexes().at(0);

	this->service.resolveIssue(selectedIssue, this->userName);
}
