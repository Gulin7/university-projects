#pragma once

#include <QWidget>
#include "ui_PresenterWindowList.h"
#include "Service.h"

class PresenterWindowList : public QWidget
{
	Q_OBJECT

public:
	PresenterWindowList(Service& service, QWidget *parent = nullptr);
	~PresenterWindowList();

public slots:
	void addQuestion();
	void handleDataChange();

private:
	Ui::PresenterWindowListClass ui;
	Service& service;
};
