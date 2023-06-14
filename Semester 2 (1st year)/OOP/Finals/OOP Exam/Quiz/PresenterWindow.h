#pragma once

#include <QWidget>
#include "ui_PresenterWindow.h"

#include "Service.h"
#include "Observer.h"

class PresenterWindow : public QWidget, public Observer
{
	Q_OBJECT

public:
	PresenterWindow(Service& service, QWidget *parent = nullptr);
	~PresenterWindow();

	void populateQuestionsList();
	void update() override;

public slots:
	void addQuestion();

private:
	Ui::PresenterWindowClass ui;

	Service& service;
};
