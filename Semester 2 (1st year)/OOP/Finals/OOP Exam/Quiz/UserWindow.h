#pragma once

#include <QtWidgets/QWidget>
#include <unordered_map>

#include "ui_UserWindow.h"

#include "Service.h"
#include "Observer.h"

using std::unordered_map;

class UserWindow : public QWidget, public Observer
{
    Q_OBJECT

public:
    UserWindow(Service& service, string userName, QWidget *parent = nullptr);
    ~UserWindow();

    void populateQuestionList();

    void update() override;

    void updateScore();

public slots:
    void answerQuestion();
    void checkForDisable();

private:
    Ui::UserWindowClass ui;
    Service& service;
    string userName;
    unordered_map<int, bool> answered;
    int score;
};
