#include "ParticipantUI.h"

ParticipantUI::ParticipantUI(Repository& repo, string userName, QWidget *parent)
	: QMainWindow(parent), repo(repo), userName(userName)
{
	ui.setupUi(this);
	
	setWindowTitle(QString::fromStdString(userName));

	this->populateList();

}

void ParticipantUI::update()
{
	this->populateList();
	int score = repo.findParticipantByName(userName).getScore();
	ui.scoreLabel->setText(QString::fromStdString(std::to_string(score)));
}

void ParticipantUI::populateList()
{
	ui.questionListWidget->clear();
	for (auto& quest : repo.getAllQuestions()) {
		QListWidgetItem* item = new QListWidgetItem(QString::fromStdString(quest.toStringNoAnswer()));
		item->setData(Qt::UserRole, QString::fromStdString(std::to_string(quest.getId())));
		int questId = quest.getId();
		for (int i = 0;i<questionAnswered.size();i++) {
			if(questId == questionAnswered[i])
			{
				if (answers[i]==1) {
					QBrush brush(Qt::green);
					item->setBackground(brush);
				}
			}
		}
		ui.questionListWidget->addItem(item);
	}
}

void ParticipantUI::answerQuestion() {
	if (ui.questionListWidget->currentItem() == nullptr) {
		QMessageBox::warning(this, "Warning", QString::fromStdString("No question selected!"));
		return;
	}	
	int id = ui.questionListWidget->currentItem()->data(Qt::UserRole).toInt();
	Question question(1,"","",1);
	for (auto& quest : repo.getAllQuestions())
		if (quest.getId() == id)
			question = quest;
	string answer = ui.answerLineEdit->text().toStdString();
	if (answer.size() == 0)
		QMessageBox::warning(this, "Warning", QString::fromStdString("No answer!"));
	else {
		for (auto& elem : questionAnswered) {
			if (question.getId() == elem)
				QMessageBox::warning(this, "Warning", QString::fromStdString("Already answered!"));
		}
		if (question.getAnswer() == answer) {
			QListWidgetItem* item = ui.questionListWidget->currentItem();
			QBrush brush(Qt::green);
			item->setBackground(brush);
			repo.increasePartScore(this->userName, question.getScore());
			this->questionAnswered.push_back(question.getId());
			this->answers.push_back(1);
		}
		else {
			this->questionAnswered.push_back(question.getId());
			this->answers.push_back(0);
		}
	}
	repo.notify();
}

