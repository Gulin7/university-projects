#pragma once
#include "AdministratorService.h"
#include "UserService.h"
#include <QtWidgets/QApplication>
#include <QtWidgets/qlabel.h>
#include <QtWidgets/qpushbutton.h>
#include <QtWidgets/qboxlayout.h>
#include <QtWidgets/qlineedit.h>
#include <QtWidgets/qformlayout.h>
#include <qdebug.h>
#include <qmessagebox.h>
#include <QtWidgets/qlistwidget.h>
#include <vector>
#include <string>
#include <qtimer.h>
#include <QtWidgets/qtablewidget>
#include "a89qt.h"
#include <QApplication>
#include <QTabWidget>
#include <QDialog>
#include <QPushButton>
#include <QVBoxLayout>
#include <QStackedWidget>
#include <QtWidgets/QComboBox>

class AdminGUI : public QWidget {
Q_OBJECT
private:
    AdministratorService& adminService;

    QTabWidget* adminTabWidget;
    QListWidget* events;

    QLineEdit* editTitle;
    QLineEdit* editDescription;
    QLineEdit* editDay;
    QLineEdit* editMonth;
    QLineEdit* editYear;
    QLineEdit* editMinute;
    QLineEdit* editHour;
    QLineEdit* editNumberOfPeople;
    QLineEdit* editLink;

    QPushButton* addEventButton;
    QPushButton* removeEventButton;
    QPushButton* updateEventButton;

    void addEvent();
    void removeEvent();
    void updateEvent();
    void reloadList();
    std::string getCurrentEventTitle(); //title and description
    std::string getCurrentEventDescription();
    void connectSignals();

public:
    explicit AdminGUI(AdministratorService& admin);
};

class UserGUI:public QWidget {
Q_OBJECT
private:
    UserService& userService;
    AdministratorService& adminService;

    

    QTabWidget* userTabWidget;
    QLabel* event;
    QLabel* eventLink;
    QListWidget* eventlist;
    int current{};
    QComboBox* editMonthComboBox;

    QPushButton* addEventButton;
    QPushButton* skipEventButton;
    QPushButton* getEventButton;
    QPushButton* changeFileTypeButton;
    QPushButton* openFileButton;

    void connectSignals();
    void showNextEvent();
    void reloadEventlist();
    void addEvent();
    void skipEvent();
    void changeFile();
    void getEvents();
    void openFile();

public:
    explicit UserGUI(UserService& user, AdministratorService& admin);
    int currentPosition = 0;
    int currentMonth = 10;
};


class GUI : public QWidget
{
public:
    // Constructor
    explicit GUI(AdministratorService& admin, UserService& user, QWidget* parent = nullptr);
};

