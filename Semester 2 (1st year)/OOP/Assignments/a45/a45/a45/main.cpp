#include <iostream>
#include "Ui.h"
#include "Tests.h"
#include <crtdbg.h>

int main() {
	{
		runAllTests();

		std::vector<Event> events;
		std::vector<Event> events_user;

		Repository repository{ events };
		Repository repository_user{ events_user };

		AdministratorService administratorService{ repository };
		administratorService.generateEvents();

		UserService userService{ repository_user };

		Ui ui{ administratorService, userService };

		ui.runUi();
	}

	_CrtDumpMemoryLeaks();
}