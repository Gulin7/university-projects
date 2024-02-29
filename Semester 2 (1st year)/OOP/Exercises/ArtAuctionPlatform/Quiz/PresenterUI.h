#pragma once

#include <QMainWindow>
#include "ui_PresenterUI.h"
#include "Observer.h"
#include "Repository.h"
#include <QMessageBox>

class PresenterUI : public QMainWindow, public Observer
{
	Q_OBJECT

public:
	PresenterUI(Repository& repo, QWidget *parent = nullptr);

	void update() override;

	void populateList();

	~PresenterUI();

private:
	Ui::PresenterUIClass ui;
	Repository& repo;
	
public slots:
	void addQuestion();
};
