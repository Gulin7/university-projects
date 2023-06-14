#include "UserWindow.h"
#include "PresenterWindow.h"
#include <QtWidgets/QApplication>

#include "ParticipantsRepository.h"
#include "QuestionsRepository.h"

#include "PresenterWindowList.h"
#include "UserWindowList.h"

#include "Testing.h"

int main(int argc, char *argv[])
{

    /*Testing tests;
    tests.testAll();*/

    QApplication a(argc, argv);
    
    ParticipantsRepository participants{ "participants.txt" };
    QuestionsRepository questions{ "questions.txt" };

    Service service{ participants, questions };


    PresenterWindowList window{ service };
    UserWindowList userWindow{ service };

    QObject::connect(&service, &Service::dataChangedSignal, &window, &PresenterWindowList::handleDataChange);

    window.show();
    userWindow.show();
    /*UserWindow* users[100];

    int index = 0;
    for (auto participant : participants.getAll())
    {
        users[index] = new UserWindow{ service, participant.getName() };
        service.registerObserver(users[index]);

        users[index]->show();
        index++;
    }

    PresenterWindow* presenter = new PresenterWindow{ service };
    service.registerObserver(presenter);

    presenter->show();*/

    return a.exec();
}
