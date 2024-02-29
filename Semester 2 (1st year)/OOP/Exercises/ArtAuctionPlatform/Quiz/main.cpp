#include <QtWidgets/QApplication>
#include "ParticipantUI.h"
#include "PresenterUI.h"
#include "Repository.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    
    Repository repo;

    vector<ParticipantUI*> participantUi;
    PresenterUI* presenterUi = new PresenterUI{ repo };

    for (auto& participant : repo.getAllParticipants()) {
        participantUi.push_back( new ParticipantUI(repo, participant.getName()));
    }

    for (auto& window : participantUi) {
		repo.addObserver(window);
		window->show();
	}

    repo.addObserver(presenterUi);
    presenterUi->show();

    return a.exec();
}
