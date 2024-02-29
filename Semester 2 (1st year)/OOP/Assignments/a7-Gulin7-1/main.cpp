#include <iostream>
#include <crtdbg.h>
#include "Ui.h"
#include "Tests.h"
#include "Exception.h"
#include "Eventlist.h"
#include "CsvEventlist.h"
#include "HtmlEventlist.h"
#include "FileEventlist.h"

int main() {
	{
		try {
			Repository repository { "Events.txt" };
			FileEventlist* file = nullptr;
			std::cout << "Pick a file type: (csv/html)?\n";
			std::string fileType;
			std::cin >> fileType;
			if (fileType == "csv")
				file = new CsvEventlist{ "Events.csv" };
			else
				file = new HtmlEventlist{ "Events.html" };

			AdministratorService adminService{ repository };
			UserService userService{ repository, file };

			Ui ui{ adminService, userService };
			ui.runUi();
		}
		catch (Exception) {
			std::cout << "File couldn't be opened! " << std::endl;
			return 1;
		}
	}
	_CrtDumpMemoryLeaks();
}