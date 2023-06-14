#pragma once

#include <QtWidgets/QWidget>
#include "ui_writerWindow.h"

#include "Service.h"

class writerWindow : public QWidget
{
    Q_OBJECT

public:
    writerWindow(QAbstractItemModel* model, Service& service, string writerName, QWidget *parent = nullptr);
    ~writerWindow();

    void connectSignals();

public slots:
    void addIdea();
    void checkForDisableReviseButton();
    void reviseIdea();

private:
    Ui::writerWindowClass ui;

    string writerName;
    Service& service;
};
