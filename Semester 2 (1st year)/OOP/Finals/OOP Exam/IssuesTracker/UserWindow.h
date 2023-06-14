#pragma once

#include <QWidget>
#include <QAbstractItemModel>

#include "ui_UserWindow.h"

#include "Service.h"

class UserWindow : public QWidget
{
	Q_OBJECT

public:
	UserWindow(QAbstractItemModel* model, Service& service, string userName, QWidget *parent = nullptr);
	~UserWindow();

public slots:

	void addIssue();
	void removeIssue();
	void checkForDisableButton();
	void resolveIssue();

private:
	Ui::UserWindowClass ui;

	Service& service;
	string userName;
	User currentUser;
};
