#include "GUI.h"
#include "Exception.h"
#include <QDesktopServices>
#include "HtmlEventlist.h"
#include "CsvEventlist.h"
#include "FileEventlist.h"
#include <QApplication>
#include <QScreen>
#include <QTabWidget>
#include <sstream>

AdminGUI::AdminGUI(AdministratorService& admin) : adminService{ admin }
{
    this->setWindowTitle("Event application");
    this->adminTabWidget = new QTabWidget;
    this->setMinimumWidth(700);
    this->setMinimumHeight(300);
    auto* parentLayout = new QVBoxLayout{ this };

    parentLayout->addWidget(this->adminTabWidget);
    /*
    // Center the adminTabWidget on the screen
    QRect screenGeometry = QGuiApplication::primaryScreen()->geometry();
    int screenWidth = screenGeometry.width();
    int screenHeight = screenGeometry.height();
    int tabWidth = this->width();
    int tabHeight = this->height();
    int tabX = screenWidth / 2 - tabWidth / 2;
    int tabY = screenHeight / 2 - tabHeight / 2;
    this->move(tabX, tabY);
    */
    auto* generalWindow = new QWidget;
    auto* layout = new QHBoxLayout{ generalWindow };
    this->adminTabWidget->addTab(generalWindow, "Admin Mode");

    auto* leftSide = new QWidget;
    layout->addWidget(leftSide);
    auto* leftVBox = new QVBoxLayout(leftSide);

    auto* eventsName = new QLabel{ "Events" };
    leftVBox->addWidget(eventsName);

    this->events = new QListWidget;
    this->events->setSelectionMode(QAbstractItemView::SingleSelection);
    QFont font = events->font();
    font.setPointSize(20);
    events->setFont(font);

    reloadList();
    leftVBox->addWidget(this->events);

    auto* eventData = new QWidget;
    auto* fieldsForm = new QFormLayout{ eventData };
    leftVBox->addWidget(eventData);

    this->editTitle = new QLineEdit;
    auto* titleLabel = new QLabel{ "Title: " };
    this->editDescription = new QLineEdit;
    auto* descriptionLabel = new QLabel{ "Description: " };
    this->editDay = new QLineEdit;
    auto* dayLabel = new QLabel{ "Day: " };
    this->editMonth = new QLineEdit;
    auto* monthLabel = new QLabel{ "Month: " };
    this->editYear = new QLineEdit;
    auto* yearLabel = new QLabel{ "Year: " };
    this->editMinute = new QLineEdit;
    auto* minuteLabel = new QLabel{ "Minute: " };
    this->editHour = new QLineEdit;
    auto* hourLabel = new QLabel{ "Hour: " };
    this->editNumberOfPeople = new QLineEdit;
    auto* numberOfPeopleLabel = new QLabel{ "NumberOfPeople: " };
    this->editLink = new QLineEdit;
    auto* linkLabel = new QLabel{ "Link: " };
    fieldsForm->addRow(titleLabel, this->editTitle);
    fieldsForm->addRow(descriptionLabel, this->editDescription);
    fieldsForm->addRow(dayLabel, this->editDay);
    fieldsForm->addRow(monthLabel, this->editMonth);
    fieldsForm->addRow(yearLabel, this->editYear);
    fieldsForm->addRow(minuteLabel, this->editMinute);
    fieldsForm->addRow(hourLabel, this->editHour);
    fieldsForm->addRow(numberOfPeopleLabel, this->editNumberOfPeople);
    fieldsForm->addRow(linkLabel, this->editLink);
    //
    auto* rightSide = new QWidget;
    layout->addWidget(rightSide);
    auto* rightVBox = new QVBoxLayout(rightSide);
    auto* buttonsLayout = new QVBoxLayout;
    this->addEventButton = new QPushButton("Add event");
    this->removeEventButton = new QPushButton("Remove event");
    this->updateEventButton = new QPushButton("Update event");

    buttonsLayout->addWidget(this->addEventButton);
    buttonsLayout->addWidget(this->removeEventButton);
    buttonsLayout->addWidget(this->updateEventButton);

    rightVBox->addLayout(buttonsLayout);

    connectSignals();
}

void AdminGUI::addEvent()
{
    try {
        std::string errors;
        std::string title = editTitle->text().toStdString();
        if (title.empty()) {
            errors += "Title is empty! :(\n";
        }
        std::string description = editDescription->text().toStdString();
        if (description.empty()) {
            errors += "Description is empty! :(\n";
        }
        std::string link = editLink->text().toStdString();
        if (link.empty()) {
            errors += "Title is empty! :(\n";
        }
        bool checkResponse = false;
        int day = editDay->text().toInt(&checkResponse);
        if (!checkResponse) {
            errors += "Invalid day\n";
        }
        checkResponse = false;
        int month = editMonth->text().toInt(&checkResponse);
        if (!checkResponse) {
            errors += "Invalid month\n";
        }
        checkResponse = false;
        int year = editYear->text().toInt(&checkResponse);
        if (!checkResponse) {
            errors += "Invalid year\n";
        }
        checkResponse = false;
        int minute = editMinute->text().toInt(&checkResponse);
        if (!checkResponse) {
            errors += "Invalid minute\n";
        }
        checkResponse = false;
        int hour = editHour->text().toInt(&checkResponse);
        if (!checkResponse) {
            errors += "Invalid hour\n";
        }
        checkResponse = false;
        int numberOfPeople = editNumberOfPeople->text().toInt(&checkResponse);
        if (!checkResponse) {
            errors += "Invalid numberOfPeople\n";
        }

        if (!errors.empty()) {
            throw ExceptionGUI(errors);
        }

        auto item = events->selectedItems().at(0);
        auto data = item->text().toStdString();
        Date date{ year, month, day };
        Time time{ hour, minute };
        adminService.addEvent(title, description, date, time, numberOfPeople, link);

        reloadList();

    }
    catch (ExceptionGUI& errorGUI) {
        QMessageBox::warning(this, "Warning", QString::fromStdString(errorGUI.what()));
    }
    catch (Exception& error) {
        QMessageBox::warning(this, "Warning", QString::fromStdString(error.what()));
    }

}

void AdminGUI::removeEvent()
{
    try {
        auto selectedEvent = events->selectedItems();
        if (selectedEvent.empty()) {
            throw ExceptionGUI("You did not select an event :P\n");
        }
        adminService.removeEvent(getCurrentEventTitle(), getCurrentEventDescription());
        reloadList();
    }
    catch (ExceptionGUI& errorGUI) {
        QMessageBox::warning(this, "Warning", QString::fromStdString(errorGUI.what()));
    }
    catch (Exception& error) {
        QMessageBox::warning(this, "Warning", QString::fromStdString(error.what()));
    }
}

void AdminGUI::updateEvent()
{
    try {
        std::string errors;
        std::string title = editTitle->text().toStdString();
        if (title.empty()) {
            errors += "Title is empty! :(\n";
        }
        std::string description = editDescription->text().toStdString();
        if (description.empty()) {
            errors += "Description is empty! :(\n";
        }
        std::string link = editLink->text().toStdString();
        if (link.empty()) {
            errors += "Title is empty! :(\n";
        }
        bool checkResponse = false;
        int day = editDay->text().toInt(&checkResponse);
        if (!checkResponse) {
            errors += "Invalid day\n";
        }
        checkResponse = false;
        int month = editMonth->text().toInt(&checkResponse);
        if (!checkResponse) {
            errors += "Invalid month\n";
        }
        checkResponse = false;
        int year = editYear->text().toInt(&checkResponse);
        if (!checkResponse) {
            errors += "Invalid year\n";
        }
        checkResponse = false;
        int minute = editMinute->text().toInt(&checkResponse);
        if (!checkResponse) {
            errors += "Invalid minute\n";
        }
        checkResponse = false;
        int hour = editHour->text().toInt(&checkResponse);
        if (!checkResponse) {
            errors += "Invalid hour\n";
        }
        checkResponse = false;
        int numberOfPeople = editNumberOfPeople->text().toInt(&checkResponse);
        if (!checkResponse) {
            errors += "Invalid numberOfPeople\n";
        }

        if (!errors.empty()) {
            throw ExceptionGUI(errors);
        }

        auto item = events->selectedItems().at(0);
        auto data = item->text().toStdString();
        Date date{ year, month, day };
        Time time{ hour, minute };
        adminService.updateEvent(getCurrentEventTitle(), getCurrentEventDescription(), title, description, date, time, numberOfPeople, link);

        reloadList();

    }
    catch (ExceptionGUI& errorGUI) {
        QMessageBox::warning(this, "Warning", QString::fromStdString(errorGUI.what()));
    }
    catch (Exception& error) {
        QMessageBox::warning(this, "Warning", QString::fromStdString(error.what()));
    }
}

void AdminGUI::reloadList()
{
    events->clear();

    for (auto& event : adminService.getAllEvents()) {
        auto* item = new QListWidgetItem(QString::fromStdString(event.toString()));
        events->addItem(item);
    }
}

std::string AdminGUI::getCurrentEventTitle()
{
    std::string title;
    auto items = events->selectedItems();
    if (!items.empty()) {
        auto data = items.at(0)->text().toStdString();
        size_t titlePosition = data.find("Title: ");
        if (titlePosition != std::string::npos) {
            std::string titleAux = data.substr(titlePosition + 7); // Skip "Title: "
            size_t spacePosition = titleAux.find(" |");
            title = titleAux.substr(0, spacePosition);
        }
    }
    //QMessageBox::information(this, "MAAAAAAAAMAAAAAAAAA", QString::fromStdString(title));
    return title;
}

std::string AdminGUI::getCurrentEventDescription()
{
    std::string description;
    auto items = events->selectedItems();
    if (!items.empty()) {
        auto data = items.at(0)->text().toStdString();
        size_t descriptionPosition = data.find("Description: ");
        if (descriptionPosition != std::string::npos) {
            std::string descriptionAux = data.substr(descriptionPosition + 13); // Skip to Description: "
            size_t spacePosition = descriptionAux.find(" \n|");
            description = descriptionAux.substr(0, spacePosition);
        }
    }
    //QMessageBox::information(this, "MAAAAAAAAAMAAAAAAAAA", QString::fromStdString(description));
    return description;
}


void AdminGUI::connectSignals()
{
    QObject::connect(addEventButton, &QPushButton::clicked, this, &AdminGUI::addEvent);

    QObject::connect(removeEventButton, &QPushButton::clicked, this, &AdminGUI::removeEvent);

    QObject::connect(updateEventButton, &QPushButton::clicked, this, &AdminGUI::updateEvent);

    QObject::connect(events, &QListWidget::itemSelectionChanged, this, [&]() {
        auto selectedEvent = events->selectedItems();
        if (selectedEvent.isEmpty()) {
            editTitle->setText("");
            editDescription->setText("");
            editDay->setText("");
            editMonth->setText("");
            editYear->setText("");
            editMinute->setText("");
            editHour->setText("");
            editNumberOfPeople->setText("");
            editLink->setText("");
        }
        else {
            Event event = adminService.getEventByTitle(getCurrentEventTitle());
            editTitle->setText(QString::fromStdString(event.getTitle()));
            editDescription->setText(QString::fromStdString(event.getDescription()));
            editLink->setText(QString::fromStdString(event.getLink()));
            editNumberOfPeople->setText(QString::fromStdString(std::to_string(event.getNumberOfPeople())));
            editDay->setText(QString::fromStdString(std::to_string(event.getDate().day)));
            editMonth->setText(QString::fromStdString(std::to_string(event.getDate().month)));
            editYear->setText(QString::fromStdString(std::to_string(event.getDate().year)));
            editMinute->setText(QString::fromStdString(std::to_string(event.getTime().minute)));
            editHour->setText(QString::fromStdString(std::to_string(event.getTime().hour)));
        }
        });
}
/*
START OF USER GUI
*/
void UserGUI::connectSignals()
{
    connect(addEventButton, &QPushButton::clicked, this, &UserGUI::addEvent);
    connect(removeEventButton, &QPushButton::clicked, this, &UserGUI::removeEvent);
    connect(skipEventButton, &QPushButton::clicked, this, &UserGUI::skipEvent);
    connect(getEventButton, &QPushButton::clicked, this, &UserGUI::getEvents);
    connect(changeFileTypeButton, &QPushButton::clicked, this, &UserGUI::changeFile);
    connect(openFileButton, &QPushButton::clicked, this, &UserGUI::openFile);

    connect(eventlist, &QListWidget::itemClicked, this, [](QListWidgetItem* item) {
        QDesktopServices::openUrl(QUrl(item->data(Qt::UserRole).toString()));
        });
}

void UserGUI::showNextEvent()
{
    this->currentPosition++;
    if (this->currentPosition == this->userService.getEventOfGivenMonth(this->adminService.getAllEvents(), this->editMonthComboBox->currentText().toInt()).size()) {
        this->currentPosition = 0;
    }
    Event currentEvent = this->userService.getEventOfGivenMonth(this->adminService.getAllEvents(), this->editMonthComboBox->currentText().toInt())[this->currentPosition];
    
    this->event->setText(QString::fromStdString(currentEvent.toString()));

}

void UserGUI::showCurrentEvent()
{
    Event currentEvent = this->userService.getEventOfGivenMonth(this->adminService.getAllEvents(), this->editMonthComboBox->currentText().toInt())[this->currentPosition];
    this->event->setText(QString::fromStdString(currentEvent.toString()));
}

void UserGUI::reloadEventlist()
{
    eventlist->clear();
    for (auto& event : this->userService.getEventList()->getAllEvents()) {
        auto* item = new QListWidgetItem(QString::fromStdString(event.toString()));
        item->setData(Qt::UserRole, QString::fromStdString(event.getTitle() + ';' + event.getDescription()));
        eventlist->addItem(item);
    }
}

void UserGUI::addEvent()
{
    try {      
        this->userService.addEventToList(this->userService.getEventOfGivenMonth(this->adminService.getAllEvents(), this->editMonthComboBox->currentText().toInt())[this->currentPosition]);
        this->showNextEvent();
        this->reloadEventlist();
    }
    catch (Exception& error) {
        QMessageBox::warning(this, "Warning!!!", QString::fromStdString(error.what()));
    }
    catch (ExceptionGUI& errorGUI) {
        QMessageBox::warning(this, "Warning!!!", QString::fromStdString(errorGUI.what()));
    }
}

void UserGUI::removeEvent()
{
    try {
        QList<QListWidgetItem*> selectedItems = this->eventlist->selectedItems();
        // Check if any item is selected
        if (selectedItems.isEmpty()) {
            throw Exception("Nu-i bine");
        }
        std::string data = this->eventlist->currentItem()->data(Qt::UserRole).toString().toStdString();
        std::stringstream datastream(data);
        std::vector<std::string> datavector = {};
        std::string token;
        while (getline(datastream, token, ';')) {
            datavector.push_back(token);
        }
        this->userService.removeEventFromList(datavector[0], datavector[1]);
        this->adminService.decreaseNumberOfPoeple(datavector[0], datavector[1]);
        this->reloadEventlist();
    }
    catch (Exception& error) {
        QMessageBox::warning(this, "Warning!!!", QString::fromStdString(error.what()));
    }
    catch (ExceptionGUI& errorGUI) {
        QMessageBox::warning(this, "Warning!!!", QString::fromStdString(errorGUI.what()));
    }
    catch (const std::exception& ex) {
        QMessageBox::warning(this, "Warning!!!", QString::fromStdString("Not working :P"));
    }
}

void UserGUI::skipEvent()
{
    try {
        this->showNextEvent();
    }
    catch (Exception& error) {
        QMessageBox::warning(this, "Warning!!!", QString::fromStdString(error.what()));
    }
    catch (ExceptionGUI& errorGUI) {
        QMessageBox::warning(this, "Warning!!!", QString::fromStdString(errorGUI.what()));
    }
}

void UserGUI::changeFile()
{
    if (this->userService.getFilename() == "Events.csv") {
        FileEventlist* file = new HtmlEventlist{ "Events.html" };
        UserService newUserService{ this->userService.eventRepository, file };
        newUserService.getEventList()->setEvents(this->userService.getEventList()->getAllEvents());
        this->userService = newUserService;
    }     
    else
    {
        FileEventlist* file = new CsvEventlist{ "Events.csv" };
        UserService newUserService{ this->userService.eventRepository, file };
        newUserService.getEventList()->setEvents(this->userService.getEventList()->getAllEvents());
        this->userService = newUserService;
    }
    QMessageBox::information(this, "CURRENT FILE TYPE", QString::fromStdString(this->userService.getFilename()));
}

void UserGUI::getEvents()
{
    try {
        this->currentPosition = 0;
        this->userService.getEventOfGivenMonth(this->adminService.getAllEvents(), this->editMonthComboBox->currentText().toInt());
        this->showNextEvent();

    }
    catch (Exception& error) {
        QMessageBox::warning(this, "Warning!!!", QString::fromStdString(error.what()));
    }
    catch (ExceptionGUI& errorGUI) {
        QMessageBox::warning(this, "Warning!!!", QString::fromStdString(errorGUI.what()));
    }
}

void UserGUI::openFile()
{
    try {
        this->userService.saveEventlist();
        this->userService.openEventlist();
    }
    catch (Exception& error) {
        QMessageBox::warning(this, "Warning!!!", QString::fromStdString(error.what()));
    }
    catch (ExceptionGUI& errorGUI) {
        QMessageBox::warning(this, "Warning!!!", QString::fromStdString(errorGUI.what()));
    }
}

UserGUI::UserGUI(UserService& user, AdministratorService& admin): userService{user}, adminService{admin}
{
    this->setWindowTitle("EVENTLIST");
    this->userTabWidget = new QTabWidget;
    auto* parentLayout = new QVBoxLayout{ this };
    parentLayout->addWidget(this->userTabWidget);

    auto* guiWindow = new QWidget;
    auto* layout = new QHBoxLayout{ guiWindow };
    this->userTabWidget->addTab(guiWindow, "User Mode");

    auto* leftSide = new QWidget;
    layout->addWidget(leftSide);
    auto* leftVbox = new QVBoxLayout(leftSide);

    event = new QLabel();
    QFont font = event->font();
    font.setPointSize(18);
    event->setFont(font);
    leftVbox->addWidget(event);

    auto* buttons = new QWidget;
    auto* buttonsLayout = new QVBoxLayout{ buttons };
    this->addEventButton = new QPushButton("Add To Eventlist");
    this->removeEventButton = new QPushButton("Remove from Eventlist");
    this->skipEventButton = new QPushButton("Skip");
    buttonsLayout->addWidget(this->addEventButton);
    buttonsLayout->addWidget(this->removeEventButton);
    buttonsLayout->addWidget(this->skipEventButton);
    leftVbox->addWidget(buttons);

    auto* monthButtons = new QWidget;
    auto* monthLayout = new QHBoxLayout{ monthButtons };
    auto* monthText = new QLabel("Select month: ");
    this->editMonthComboBox = new QComboBox;
    editMonthComboBox->addItem("1");
    editMonthComboBox->addItem("2");
    editMonthComboBox->addItem("3");
    editMonthComboBox->addItem("4");
    editMonthComboBox->addItem("5");
    editMonthComboBox->addItem("6");
    editMonthComboBox->addItem("7");
    editMonthComboBox->addItem("8");
    editMonthComboBox->addItem("9");
    editMonthComboBox->addItem("10");
    editMonthComboBox->addItem("11");
    editMonthComboBox->addItem("12");
    this->getEventButton = new QPushButton("Submit");
    monthLayout->addWidget(monthText);
    monthLayout->addWidget(editMonthComboBox);
    monthLayout->addWidget(this->getEventButton);
    leftVbox->addWidget(monthButtons);

    auto* rightSide = new QWidget;
    layout->addWidget(rightSide);
    auto* rightVbox = new QVBoxLayout(rightSide);

    auto* eventlistName = new QLabel{ "Eventlist" };
    rightVbox->addWidget(eventlistName);
    this->eventlist = new QListWidget;
    font = eventlist->font();
    font.setPointSize(18);
    eventlist->setFont(font);
    this->eventlist->setSelectionMode(QAbstractItemView::SingleSelection);

    rightVbox->addWidget(this->eventlist);

    this->openFileButton = new QPushButton("Open Eventlist");
    this->changeFileTypeButton = new QPushButton("Change File Type");
    rightVbox->addWidget(this->changeFileTypeButton);
    rightVbox->addWidget(this->openFileButton);


    connectSignals();
}

GUI::GUI(AdministratorService& admin, UserService& user, QWidget* parent)
{
    auto* adminGUI = new AdminGUI(admin);
    auto* userGUI = new UserGUI(user, admin);

    auto* adminButton = new QPushButton("Administrator mode");
    auto* userButton = new QPushButton("User mode");

    auto* modeLayout = new QHBoxLayout;
    modeLayout->addWidget(adminButton);
    modeLayout->addWidget(userButton);

    auto* stack = new QStackedWidget;
    stack->addWidget(adminGUI);
    stack->addWidget(userGUI);

    auto* layout = new QVBoxLayout;
    layout->addLayout(modeLayout);
    layout->addWidget(stack);

    setLayout(layout); 

    connect(adminButton, &QPushButton::clicked, stack, [stack]() {
        stack->setCurrentIndex(0);
        });
    connect(userButton, &QPushButton::clicked, stack, [stack]() {
        stack->setCurrentIndex(1);
        });
}
