#pragma once
#include "Service.h"
#include <iostream>

#define ADD_PLAYER 1
#define SHOW_PLAYERS 2
#define SHOW_IN_TEAM 3
#define EXIT 0

class Ui
{
private:
	Service service;
public:
	Ui(Service initialService);

	int inputCommand();
	std::string inputName();
	std::string inputNationality();
	std::string inputTeam();
	int inputGoals();

	void showMenu();
	void addPlayer();
	void showAllPlayers();
	void showAllInTeam();

	void runUi();
};

