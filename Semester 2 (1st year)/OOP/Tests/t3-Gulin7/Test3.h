#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_Test3.h"
#include "Service.h"

class Test3 : public QMainWindow
{
    Q_OBJECT

public:
    Test3(Service service, QWidget *parent = nullptr);
    ~Test3();

private:
    Service service;
    Ui::Test3Class ui;

    void populateList();

public slots:
    void showByCategory();
    void showByNameOrCategory();
};
