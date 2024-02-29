#include "ResearcherWindow.h"
#include <QtWidgets/QApplication>
#include "IdeasTableModel.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    Controller controller{ "ideas.txt", "researchers.txt" };

    IdeasTableModel* model = new IdeasTableModel{ controller };

    QList<ResearcherWindow*> windows;
    for (auto researcher : controller.getAllResearchers()) {
        ResearcherWindow* window = new ResearcherWindow{ model, researcher };
        window->show();
    }

    return a.exec();
}
