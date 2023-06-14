#include "UserWindow.h"
#include "stringOperations.h"

#include <QMessageBox>

UserWindow::UserWindow(Service& service, string userName, QWidget* parent)
    : QWidget(parent), currentService{ service }, userName{ userName }
{
    lastQuestionText = "";
    ui.setupUi(this);

    ui.questionsList->setCurrentRow(-1);
    
    this->showList();
    connect(ui.addQuestionButton, &QPushButton::clicked, this, &UserWindow::addQuestion);
    connect(ui.questionsList, &QListWidget::itemClicked, this, &UserWindow::displayAnswers);
    connect(ui.answersList, &QListWidget::itemClicked, this, &UserWindow::disableSpinBox);
    connect(ui.addAnswerButton, &QPushButton::clicked, this, &UserWindow::addAnswer);
    connect(ui.answerSpinBox, &QSpinBox::valueChanged, this, &UserWindow::changeNumberOfVotes);
}


UserWindow::~UserWindow()
{}

void UserWindow::update()
{
    this->showList();
    this->updateAnswers();
}

void UserWindow::showList()
{
    ui.questionsList->clear();

    vector<Question> allQuestions = this->currentService.getQuestionsSortedByAnswers();

    for (auto& question : allQuestions)
    {
        QListWidgetItem* currentItem = new QListWidgetItem{ QString::fromStdString(question.getText()) };
        ui.questionsList->addItem(currentItem);
    }

    ui.questionsList->setCurrentItem(nullptr);
}

void UserWindow::updateAnswers()
{
    QBrush yellowBrush{ QColor("yellow") };

    if (lastQuestionText == "")
        return;

    ui.answersList->clear();

    vector<Answer> answers = this->currentService.getAnswers(this->currentService.getQuestionId(lastQuestionText));

    for (auto answer : answers)
    {
        QListWidgetItem* currentItem = new QListWidgetItem{ QString::fromStdString(answer.toString()) };

        if (answer.getUserName() == this->userName)
            currentItem->setBackground(yellowBrush);

        ui.answersList->addItem(currentItem);
    }
}

void UserWindow::disableSpinBox()
{
    if (ui.questionsList->selectedItems().size() != 0)
    {
        QListWidgetItem* currentQuestion = ui.questionsList->selectedItems().at(0);
        string questionText = currentQuestion->text().toStdString();
        lastQuestionText = questionText;
    }

    QListWidgetItem* currentItem = ui.answersList->selectedItems().at(0);

    string answerUser = splitString(currentItem->text().toStdString(), '|')[1];
    int answerVotes = stoi(splitString(currentItem->text().toStdString(), '|')[3]);

    ui.answerSpinBox->setValue(answerVotes);

    if (answerUser == this->userName)
        ui.answerSpinBox->setDisabled(true);
    else
        ui.answerSpinBox->setEnabled(true);
}

void UserWindow::changeNumberOfVotes()
{
    if (ui.answersList->selectedItems().size() == 0)
    {
        QMessageBox alert;
        alert.setText(QString::fromStdString("Select one answer!"));
        alert.setWindowTitle("Error!");

        alert.exec();
        return;
    }

    QListWidgetItem* currentItem = ui.answersList->selectedItems().at(0);
    int answerId = stoi(splitString(currentItem->text().toStdString(), '|')[0]);
    int newValue = ui.answerSpinBox->value();

    this->currentService.updateAnswerNumberOfVotes(answerId, newValue);
}

void UserWindow::addAnswer()
{
    if (ui.questionsList->selectedItems().size() == 0)
    {
        QMessageBox alert;
        alert.setText(QString::fromStdString("Select one question!"));
        alert.setWindowTitle("Error!");

        alert.exec();
        return;
    }

    QListWidgetItem* currentItem = ui.questionsList->selectedItems().at(0);
    string questionText = currentItem->text().toStdString();
    lastQuestionText = questionText;

    try
    {
        int questionId = this->currentService.getQuestionId(questionText);
        string answerText = ui.answerInput->text().toStdString();

        this->currentService.addAnswer(this->userName, answerText, questionId);
    }

    catch (std::exception& e)
    {
        QMessageBox alert;
        alert.setText(QString::fromStdString(e.what()));
        alert.setWindowTitle("Error!");

        alert.exec();
    }
}

void UserWindow::displayAnswers()
{
    ui.answersList->clear();

    QBrush yellowBrush{ QColor("yellow") };

    if (ui.questionsList->selectedItems().size() == 0)
    {
        QMessageBox alert;
        alert.setText(QString::fromStdString("Select one question!"));
        alert.setWindowTitle("Error!");

        alert.exec();
        return;
    }

    QListWidgetItem* currentItem = ui.questionsList->selectedItems().at(0);

    string questionText = currentItem->text().toStdString();

    vector<Answer> answers = this->currentService.getAnswers(this->currentService.getQuestionId(questionText));

    for (auto answer : answers)
    {
        QListWidgetItem* currentItem = new QListWidgetItem{ QString::fromStdString(answer.toString()) };

        if (answer.getUserName() == this->userName)
            currentItem->setBackground(yellowBrush);

        ui.answersList->addItem(currentItem);
    }
}

void UserWindow::addQuestion()
{
    string text = ui.questionInput->text().toStdString();

    try
    {
        this->currentService.addQuestion(this->userName, text);
    }

    catch (std::exception& e)
    {
        QMessageBox alert;
        alert.setText(QString::fromStdString(e.what()));
        alert.setWindowTitle("Error!");

        alert.exec();
    }
}
