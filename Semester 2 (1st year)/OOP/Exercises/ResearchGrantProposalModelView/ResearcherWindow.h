#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_ResearcherWindow.h"
#include "Observer.h"
#include "Controller.h"

class ResearcherWindow : public QMainWindow, public Observer
{
    Q_OBJECT

public:
    ResearcherWindow(Controller& controller, string userName, QWidget *parent = nullptr);
    ~ResearcherWindow();

    void update() override;

    void populateList();

    

private:
    Ui::ResearcherWindowClass ui;
    string userName;
    Controller& controller;
    int status; // 0 if not senior, 1 if senior

public slots:
    void develop();
    void saveAll();
    void save();
    void addNewIdea();
    void acceptIdea();

};
