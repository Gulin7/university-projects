#include "UserWindow.h"
#include "StringOperations.h"

#include <string>
#include <QMessageBox>

UserWindow::UserWindow(Service& service, string userName, QWidget *parent)
    : QWidget(parent), service{ service }, userName{ userName }
{
    ui.setupUi(this);
    ui.scoreLabel->setAlignment(Qt::AlignCenter);

    this->score = 0;

    this->setWindowTitle(QString::fromStdString(this->userName));

    this->populateQuestionList();
    this->updateScore();
}

UserWindow::~UserWindow()
{}

void UserWindow::populateQuestionList()
{
    ui.questionsList->clear();

    // QBrush greenBrush{ QColor{"green"} };

    vector<Question> allQuestions = this->service.getAllQuestionsSortedByScore();

    for (auto question : allQuestions)
    {
        if (answered.find(question.getId()) == answered.end())
            answered.insert({ question.getId(), false });

        string questionAsString = std::to_string(question.getId()) + " | " +
            question.getText() + " | " + std::to_string(question.getScore());

        QListWidgetItem* currentQuestion = new QListWidgetItem{ QString::fromStdString(questionAsString) };
       
        if (answered[question.getId()] == true)
            currentQuestion->setBackground(Qt::green);
        
        ui.questionsList->addItem(currentQuestion);
    }
}

void UserWindow::update()
{
    this->populateQuestionList();
}

void UserWindow::updateScore()
{
    string scoreString = "Your score is: " + std::to_string(this->score);

    ui.scoreLabel->setText(QString::fromStdString(scoreString));

    this->service.updateParticipantScore(this->userName, this->score);
}

void UserWindow::checkForDisable()
{
    QListWidgetItem* selectedQuestion = ui.questionsList->selectedItems().at(0);

    int questionId = stoi(splitString(selectedQuestion->text().toStdString())[0]);

    if (answered[questionId] == true)
        ui.answerButton->setDisabled(true);

    else
        ui.answerButton->setEnabled(true);
}

void UserWindow::answerQuestion()
{
    if (ui.questionsList->selectedItems().size() == 0)
    {
        QMessageBox alert;
        alert.setText("Please select a question from the list!");

        alert.exec();
        return;
    }

    QListWidgetItem* selectedQuestion = ui.questionsList->selectedItems().at(0);
    int questionId = stoi(splitString(selectedQuestion->text().toStdString())[0]);

    if (ui.answerInput->text().toStdString() == "")
    {
        QMessageBox alert;
        alert.setText("Please provide an answer for the question!");

        alert.exec();
        return;
    }

    answered[questionId] = true;

    string userAnswer = ui.answerInput->text().toStdString();
    Question requiredQuestion = this->service.getQuestionById(questionId);

    if (userAnswer == requiredQuestion.getCorrectAnswer())
        this->score += requiredQuestion.getScore();

    this->updateScore();
    this->update();
}
