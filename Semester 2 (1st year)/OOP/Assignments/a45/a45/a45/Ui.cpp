#include "Ui.h"
#include <string>
#include <iostream>
#include <cstdlib>


Ui::Ui(AdministratorService administratorService, UserService userService) :
	administratorService{administratorService}, userService{userService}
{
}

void Ui::addEvent()
{
	std::string title = "", description = "", link = "";
	Date date{ 1,1,2023 };
	Time time{ 0,0 };
	int numberOfPeople = 0;

	std::cout << "Enter a title: ";
	std::cin.ignore();
	std::getline(std::cin, title);

	std::cout << "Enter a description: ";
	std::getline(std::cin, description);

	std::cout << "Date: \n";
	std::cout << "Day: ";
	std::cin >> date.day;
	std::cout << "Month: ";
	std::cin >> date.month;
	std::cout << "Year: ";
	std::cin >> date.year;

	std::cout << "Time: \n";
	std::cout << "Minutes: ";
	std::cin >> time.minute;
	std::cout << "Hour: ";
	std::cin >> time.hour;

	std::cout << "Number of people: ";
	std::cin >> numberOfPeople;

	std::cout << "Link: ";
	std::cin.ignore();
	std::getline(std::cin, link);

	bool check = this->administratorService.addEventToService(title, description, date, time, numberOfPeople, link);
	if (check == true)
		std::cout << "Event added!\n";
	else
		std::cout << "Event already exists!\n";
}

void Ui::removeEvent()
{
	std::string title = "", description = "";

	std::cout << "Enter a title: ";
	std::cin.ignore();
	std::getline(std::cin, title);

	std::cout << "Enter a description: ";
	std::getline(std::cin, description);

	bool check = this->administratorService.removeEventFromService(title, description);
	if (check == true)
		std::cout << "Event does not exist!\n";
	else
		std::cout << "Event removed!\n";
}

void Ui::updateEvent()
{
	std::string title = "", description = "";

	std::cout << "Enter a title: ";
	std::cin.ignore();
	std::getline(std::cin, title);

	std::cout << "Enter a description: ";
	std::getline(std::cin, description);

	std::string newTitle = "", newDescription = "", newLink = "";
	Date newDate{ 1,1,2023 };
	Time newTime{ 0,0 };
	int newNumberOfPeople = 0;

	std::cout << "Enter a title: ";
	//std::cin.ignore();
	std::getline(std::cin, newTitle);

	std::cout << "Enter a description: ";
	std::getline(std::cin, newDescription);

	std::cout << "Date: \n";
	std::cout << "Day: ";
	std::cin >> newDate.day;
	std::cout << "Month: ";
	std::cin >> newDate.month;
	std::cout << "Year: ";
	std::cin >> newDate.year;

	std::cout << "Time: \n";
	std::cout << "Minutes: ";
	std::cin >> newTime.minute;
	std::cout << "Hour: ";
	std::cin >> newTime.hour;

	std::cout << "Number of people: ";
	std::cin >> newNumberOfPeople;

	std::cout << "Link: ";
	std::cin.ignore();
	std::getline(std::cin, newLink);

	bool check = this->administratorService.updateEventInService(title, description, newTitle, newDescription, newDate, newTime, newNumberOfPeople, newLink);
	if (check == false)
		std::cout << "Event does not exist!\n";
	else
		std::cout << "Event updated!\n";
}

void Ui::displayEvents()
{
	DynamicVector<Event>  events = this->administratorService.getAllEvents();
	for (int index = 0; index < events.getSize(); index++)
	{
		Event event = events.getElement(index);
		std::cout << "#" << index + 1 << std::endl;
		event.showEvent();
	}
}

void Ui::showAdministratorMenu()
{
	std::cout << "\n  ADMINISTRATOR MENU \n";
	std::cout << "1. Add an event \n";
	std::cout << "2. Remove an event \n";
	std::cout << "3. Update an event \n";
	std::cout << "4. Display events \n";
	std::cout << "0. Exit admin mode \n";
}

void Ui::administratorMode()
{
	int option;
	while (true) {
		showAdministratorMenu();
		std::cout << "\nEnter your option: ";
		std::cin >> option;
		switch (option)
		{
		case 1:
			addEvent();
			break;
		case 2:
			removeEvent();
			break;
		case 3:
			updateEvent();
			break;
		case 4:
			displayEvents();
			break;
		case 0:
			std::cout << "You left admin mode! \n";
			return;
		default:
			std::cout << "Invalid option!\n";
			break;
		}
	}
	return;
}

void Ui::searchByMonth()
{
	int month;
	
	std::cout << "\nSearch a month: ";
	std::cin >> month;

	DynamicVector<Event> foundEvents = this->userService.getEventOfGivenMonth(this->administratorService.getAllEvents(), month);
	
	int currentPosition = 0;
	while (true) {
		if (currentPosition >= foundEvents.getSize())
		{
			std::cout << "No events left.\n";
			return;
		}
		Event currentEvent = foundEvents.getElement(currentPosition);
		currentEvent.showEvent();

		std::cout << "Do you want to add this event to your event list? 1=yes, 2=no.\n";
		std::cout << "Enter 0 to leave.\n";

		int option;

		while (true)
		{
			std::cout << ">>>";
			std::cin >> option;
			if (option == 1) {
				bool check = this->userService.addEventToList(currentEvent);
				if (check == true)
					std::cout << "Event added!\n";
				else
					std::cout << "Event already in event list!\n";
				currentPosition++;
				break;
			}
			else if (option == 2) {
				currentPosition++;
				break;
			}
			else if (option == 0) {
				std::cout << "Search finished!\n";
				return;
			}
			else
				std::cout << "Invalid!!!";
		}
		std::cout << '\n';
	}
	return;
}

void Ui::removeEventFromEvenList()
{
	std::string title = "", description = "";
	int option;

	std::cout << "Title of the event you want to remove: ";
	std::cin.ignore();
	std::getline(std::cin, title);

	std::cout << "Description of the event you want to remove: ";
	std::getline(std::cin, description);

	bool check = this->userService.removeEventFromList(title, description);
	if (check == false)
		std::cout << "Event does not exist!\n";
	else
		std::cout << "Event removed!\n";
}

void Ui::showEventList()
{
	DynamicVector <Event> events = this->userService.getEventList();
	for (int index = 0; index < events.getSize(); index++) {
		Event event = events.getElement(index);
		std::cout << "#" << index + 1 << std::endl;
		event.showEvent();
	}
}

void Ui::showUserMenu()
{
	std::cout << "\n USER MENU \n";
	std::cout << "1. Search events \n";
	std::cout << "2. Remove event \n";
	std::cout << "3. Display event list \n";
	std::cout << "0. Exist user mode \n";
}

void Ui::userMode()
{
	int option;
	showUserMenu();
	while (true) {
		std::cout << "Enter an option!\n";
		std::cin >> option;
		//if (std::cin.fail() || option < 0 || option>3) {
			//std::cout << "Invalid input!\n";
			//std::cin.clear();
			//continue;
		//}
		switch (option)
		{
		case 1:
			searchByMonth();
			break;
		case 2:
			removeEventFromEvenList();
			break;
		case 3:
			showEventList();
			break;
		case 0:
			std::cout << "You left the user mode!\n";
			return;
		default:
			std::cout << "Invalid option! \n";
			break;
		}
	}
	return;
}

void Ui::runUi()
{
	std::cout << "Welcome to my app!\n";
	std::cout << "What mode do u want to enter? (admin=1, user=2, exit=0)\n";
	int option;
	while (true) {
		std::cout << "Enter mode: ";
		std::cin >> option;
		if (option == 1)
			administratorMode();
		else if (option == 2)
			userMode();
		else if (option == 0)
		{
			std::cout << "Byebye!";
			break;
		}
		else
			std::cout << "Invalid option!\n";
	}
	return;
}