#include "PresenterWindow.h"

#include <QMessageBox>

PresenterWindow::PresenterWindow(Service& service, QWidget *parent)
	: QWidget(parent), service{ service }
{
	ui.setupUi(this);

	this->populateQuestionsList();

	this->setWindowTitle("Presenter");
}

PresenterWindow::~PresenterWindow()
{}

void PresenterWindow::populateQuestionsList()
{
	ui.questionsList->clear();

	vector<Question> allQuestions = this->service.getAllQuestionsSortedById();

	for (auto question : allQuestions)
	{
		QListWidgetItem* currentQuestion = new QListWidgetItem{ QString::fromStdString(question.toString()) };

		ui.questionsList->addItem(currentQuestion);
	}
}

void PresenterWindow::update()
{
	this->populateQuestionsList();
}

void PresenterWindow::addQuestion()
{
	if (ui.questionIdInput->text() == "")
	{
		QMessageBox alert;

		alert.setText("Please provide an id!");
		alert.exec();

		return;
	}

	if (ui.questionTextInput->text() == "")
	{
		QMessageBox alert;

		alert.setText("Please provide the question text!");
		alert.exec();

		return;
	}

	if (ui.questionScoreInput->text() == "")
	{
		QMessageBox alert;

		alert.setText("Please provide a score!");
		alert.exec();

		return;
	}

	int questionId = stoi(ui.questionIdInput->text().toStdString());
	string questionText = ui.questionTextInput->text().toStdString();
	string questionAnswer = ui.questionAnswerInput->text().toStdString();
	int questionScore = stoi(ui.questionScoreInput->text().toStdString());

	try
	{
		this->service.addQuestion(questionId, questionText, questionAnswer, questionScore);
	}

	catch (std::exception& e)
	{
		QMessageBox alert;

		alert.setText(e.what());
		alert.exec();

		return;
	}
}
