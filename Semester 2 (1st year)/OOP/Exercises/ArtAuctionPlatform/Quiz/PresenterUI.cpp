#include "PresenterUI.h"

PresenterUI::PresenterUI(Repository& repo, QWidget *parent)
	: QMainWindow(parent), repo(repo)
{
	ui.setupUi(this);

	setWindowTitle(QString::fromStdString("Presenter tab"));

	this->populateList();
}

void PresenterUI::update()
{
	this->populateList();
}

void PresenterUI::populateList()
{
	ui.questionListWidget->clear();
	for (auto& quest : repo.getAllQuestions()) {
		QListWidgetItem* item = new QListWidgetItem(QString::fromStdString(quest.toString()));
		ui.questionListWidget->addItem(item);
	}
}

void PresenterUI::addQuestion() {
	int id = ui.idLineEdit->text().toInt();
	string text = ui.textLineEdit->text().toStdString();
	string answer = ui.answerLineEdit->text().toStdString();
	int score = ui.scoreLineEdit->text().toInt();

	if (text == "" || answer == "" || score < 0 || id < 0) {
		QMessageBox::warning(this, "Warning", QString::fromStdString("Invalid question!"));
		return;
	}

	for(auto& quest: repo.getAllQuestions())
		if (quest.getId() == id) {
			QMessageBox::warning(this, "Warning", QString::fromStdString("Invalid question id!"));
			return;
		}
	
	Question newQuestion(id, text, answer, score);
	repo.addQuestion(newQuestion);
	repo.saveToFileQuestion();
	repo.notify();
}

PresenterUI::~PresenterUI()
{}
