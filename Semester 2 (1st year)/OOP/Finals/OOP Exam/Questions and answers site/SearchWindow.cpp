#include "SearchWindow.h"

SearchWindow::SearchWindow(Service& service, QWidget *parent)
	: QWidget(parent), service{ service }
{
	ui.setupUi(this);
	this->setWindowTitle("Search");

	connect(ui.questionInput, &QLineEdit::textChanged, this, &SearchWindow::update);
}

SearchWindow::~SearchWindow()
{}

void SearchWindow::update()
{
	string questionText = ui.questionInput->text().toStdString();

	Question matchedQuestion = this->service.getMatchedQuestion(questionText);
	vector<Answer> answers = this->service.getAnswers(matchedQuestion.getId());

	ui.matchQuestionList->clear();

	QListWidgetItem* questionItem = new QListWidgetItem{ QString::fromStdString(matchedQuestion.getText()) };

	ui.matchQuestionList->addItem(questionItem);

	for (int i = 0; i < 3 && i < answers.size(); i++)
	{
		QListWidgetItem* answerItem = new QListWidgetItem{ QString::fromStdString(answers[i].getAnswerText()) };
		ui.matchQuestionList->addItem(answerItem);
	}
}