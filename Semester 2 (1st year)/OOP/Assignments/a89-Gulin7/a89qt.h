#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_a89qt.h"

class a89qt : public QMainWindow
{
    Q_OBJECT

public:
    a89qt(QWidget *parent = nullptr);
    ~a89qt();

private:
    Ui::a89qtClass ui;
};
