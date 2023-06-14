#pragma once

#include <QtWidgets/QWidget>
#include "ui_UserWindow.h"

#include "Service.h"
#include "Observer.h"

class UserWindow : public QWidget, public Observer
{
    Q_OBJECT

public:
    UserWindow(Service& service, string userName, QWidget *parent = nullptr);
    ~UserWindow();

    void update();
    void showList();

    void updateAnswers();

public slots:
    void addQuestion();
    void displayAnswers();
    void addAnswer();
    void disableSpinBox();
    void changeNumberOfVotes();


private:
    Service& currentService;
    string userName;

    string lastQuestionText;
    Ui::UserWindowClass ui;
};
