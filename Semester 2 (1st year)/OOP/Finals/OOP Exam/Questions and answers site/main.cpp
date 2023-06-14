#include "UserWindow.h"
#include <QtWidgets/QApplication>

#include "UserRepository.h"
#include "QuestionsRepository.h"
#include "AnswerRepository.h"
#include "Service.h"

#include "SearchWindow.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    UserRepository userRepo{ "users.txt" };
    QuestionsRepository questionsRepo{ "questions.txt" };
    AnswerRepository answerRepo{ "answers.txt" };
    Service service{ userRepo, questionsRepo, answerRepo };

    const int usersCount = userRepo.getAll().size();

    UserWindow* users[100];

    int index = 0;

    for (auto user : userRepo.getAll())
    {
        users[index] = new UserWindow{ service, user.getName() };

        service.registerObserver(users[index]);

        users[index]->setWindowTitle(QString::fromStdString(user.getName()));
        users[index]->show();
        index++;
    }

    SearchWindow* searchWnd = new SearchWindow{ service };
    service.registerObserver(searchWnd);
    searchWnd->show();

    return a.exec();
}
