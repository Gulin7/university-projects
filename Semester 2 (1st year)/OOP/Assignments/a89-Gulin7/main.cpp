#include "a89qt.h"
#include <QtWidgets/QApplication>
#include <iostream>
#include <crtdbg.h>
#include "AdministratorService.h"
#include "UserService.h"
#include "UnitTests.h"
#include "Exception.h"
#include "Eventlist.h"
#include "CsvEventlist.h"
#include "HtmlEventlist.h"
#include "FileEventlist.h"
#include "GUI.h"
#include <time.h>
#include <Windows.h>

int main(int argc, char *argv[])
{
    
	try {
        UnitTests tests;
        tests.runAllTests();
        // CREATE REPO + SERVICES
        Repository* repository = new Repository{};
        FileEventlist* file = new CsvEventlist{ "Events.csv" };
        AdministratorService adminService{ repository };
        UserService userService{ repository, file };

        // CREATE + START + RUN GUI
        QApplication a(argc, argv);
        QFont font("Times New Roman", 12);
        QApplication::setFont(font);

        GUI gui(adminService, userService);
        gui.show();

        return a.exec();

	}
	catch (Exception) {
		std::cout << "File couldn't be opened! " << std::endl;
		return 1;
	}
	_CrtDumpMemoryLeaks();
	
}
