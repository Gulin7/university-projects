#pragma once

#include <QMainWindow>
#include "ui_ParticipantUI.h"
#include "Observer.h"
#include "Repository.h"
#include <QMessageBox>

class ParticipantUI : public QMainWindow, public Observer
{
	Q_OBJECT

public:
	ParticipantUI(Repository& repo,string userName, QWidget *parent = nullptr);

	void update() override;

	void populateList();

	~ParticipantUI(){}

private:
	Ui::ParticipantUIClass ui;
	Repository& repo;
	string userName;
	vector<int> questionAnswered;
	vector<int> answers;

public slots:
	void answerQuestion();
};
