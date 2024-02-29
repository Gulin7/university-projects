#include <QtWidgets/QApplication>
#include "Controller.h"
#include "DoctorWindow.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    
    Controller controller{ "doctors.txt", "patients.txt" };

    vector<DoctorWindow*> windows;

    for (auto& doc : controller.getAllDoctors()) {
        DoctorWindow* window = new DoctorWindow(controller, doc);
        windows.push_back(window);
    }

    for (auto& window : windows) {
        controller.addObserver(window);
        window->show();
    }
    controller.savePatientFile();
    return a.exec();
}
