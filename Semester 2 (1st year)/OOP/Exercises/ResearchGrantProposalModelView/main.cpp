#include "ResearcherWindow.h"
#include <QtWidgets/QApplication>
#include "Controller.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    
    Controller controller("researchers.txt", "items.txt");

    vector<ResearcherWindow*> resWindows;

    for (auto& res : controller.getAllResearchers()) {
        ResearcherWindow* resWindow = new ResearcherWindow(controller, res.getName());
        resWindows.push_back(resWindow);
    }

    for (auto& window : resWindows) {
        controller.addObserver(window);
        window->show();
    }
    
    return a.exec();
}
