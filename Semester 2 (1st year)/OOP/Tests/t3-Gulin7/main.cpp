#include "Test3.h"
#include <QtWidgets/QApplication>
#include "Service.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    Service service{ "Items.txt" };
    service.readFromFile();

    Test3 w{ service };
    w.show();
    return a.exec();
}
