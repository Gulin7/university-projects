#pragma once

#include <QWidget>
#include "ui_UserWindowList.h"

#include "Service.h"

class UserWindowList : public QWidget
{
	Q_OBJECT

public:
	UserWindowList(Service& service, QWidget *parent = nullptr);
	~UserWindowList();

public slots:
	void handleDataChange();

private:
	Ui::UserWindowListClass ui;
	Service& service;
};
