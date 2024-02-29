#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_ResearcherWindow.h"
#include "Controller.h"
#include "IdeasTableModel.h"

class ResearcherWindow : public QMainWindow
{
    Q_OBJECT

public:
    ResearcherWindow(IdeasTableModel* model, Researcher res, QWidget* parent = nullptr);
    ~ResearcherWindow();

    void populateList();



private:
    Ui::ResearcherWindowClass ui;
    Researcher researcher;
    IdeasTableModel* model;

public slots:
    void develop();
    void saveAll();
    void save();
    void addNewIdea();
    void acceptIdea();

};
