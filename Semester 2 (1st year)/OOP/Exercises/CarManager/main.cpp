#include "CarManager.h"
#include <QtWidgets/QApplication>
#include "Service.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    CarManager w;
    w.show();
    return a.exec();
}
