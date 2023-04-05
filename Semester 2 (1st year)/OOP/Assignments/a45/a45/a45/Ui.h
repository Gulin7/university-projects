#pragma once
#include "AdministratorService.h"
#include "UserService.h"
#include "Event.h"

class Ui
{
private:
	AdministratorService administratorService;
	UserService userService;
public:
	Ui(AdministratorService administratorService, UserService userService);

	//ADMIN FUNCTIONALITIES
	void addEvent();
	void removeEvent();
	void updateEvent();
	void displayEvents();
	void showAdministratorMenu();
	void administratorMode();

	//USER FUNCTIONALITIES
	void searchByMonth();
	void removeEventFromEvenList();
	void showEventList();
	void showUserMenu();
	void userMode();

	void showEvent(Event event);

	void runUi();
};