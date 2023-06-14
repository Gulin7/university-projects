#include "writerWindow.h"
#include <QtWidgets/QApplication>
#include <QSortFilterProxyModel>

#include "IdeasRepository.h"
#include "WritersRepository.h"
#include "Service.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    WritersRepository writersRepo{ "writers.txt" };
    IdeasRepository ideasRepo{ "ideas.txt" };

    Service service{ writersRepo, ideasRepo };

    QSortFilterProxyModel* sortedModel = new QSortFilterProxyModel{};

    sortedModel->setSourceModel(&service);
    sortedModel->sort(3);
    sortedModel->setDynamicSortFilter(true);
    
    vector<writerWindow*> writersWindows;

    for (auto& writer : writersRepo.getAll())
    {
        writersWindows.push_back(new writerWindow{ &service, service, writer.getName()});
    }

    for (auto& window : writersWindows)
        window->show();

    return a.exec();
}
