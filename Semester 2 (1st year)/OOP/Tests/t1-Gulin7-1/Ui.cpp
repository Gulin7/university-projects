#include "Ui.h"

Ui::Ui(Service initialService): service{initialService}
{
}

int Ui::inputCommand()
{
	int command;
	std::cout << "\nEnter a command: ";
	std::cin >> command;
	return command;
}

std::string Ui::inputName()
{
	std::string name;
	std::cout << "\nEnter a name: ";
	std::cin.ignore();
	std::getline(std::cin, name);
	return name;
}

std::string Ui::inputNationality()
{
	std::string nationality;
	std::cout << "\nEnter a nationality: ";
	std::cin.ignore();
	std::getline(std::cin, nationality);
	return nationality;
}

std::string Ui::inputTeam()
{
	std::string team;
	std::cout << "\nEnter a team: ";
	std::cin.ignore();
	std::getline(std::cin, team);
	return team;
}

int Ui::inputGoals()
{
	int goals;
	std::cout << "\nEnter a number of goals: ";
	std::cin >> goals;
	return goals;
}

void Ui::showMenu()
{
	std::cout << "\n		MENU		";
	std::cout << "\n1.Add player.";
	std::cout << "\n2.Show players.";
	std::cout << "\n3.Show players in team.";
	std::cout << "\n0.Exit.";
}

void Ui::addPlayer()
{
	std::string playerName = this->inputName();
	std::string playerNationality = this->inputNationality();
	std::string playerTeam = this->inputTeam();
	int playerGoals = this->inputGoals();
	Player playerToAdd{ playerName, playerNationality, playerTeam, playerGoals };
	this->service.addPlayer(playerToAdd);
}

void Ui::showAllPlayers()
{
	std::vector<Player> allPlayers = this->service.getAllPlayers();
	for (int index = 0; index < allPlayers.size(); index++) {
		std::cout << "\n" << index + 1;
		std::cout << "\nPlayer name: " << allPlayers[index].getName();
		std::cout << "\nPlayer nationality: " << allPlayers[index].getNationality();
		std::cout << "\nPlayer team: " << allPlayers[index].getTeam();
		std::cout << "\nPlayer goals: " << allPlayers[index].getGoals();
	}
}

void Ui::showAllInTeam()
{
	std::cout << "\nGIVEN TEAM: ";
	std::string givenTeam = this->inputTeam();
	std::vector<Player> allPlayers = this->service.getAllInTeam(givenTeam);
	int totalGoals = 0;
	for (int index = 0; index < allPlayers.size(); index++) {
		std::cout << "\n" << index + 1;
		std::cout << "\nPlayer name:" << allPlayers[index].getName();
		std::cout << "\nPlayer nationality:" << allPlayers[index].getNationality();
		std::cout << "\nPlayer team:" << allPlayers[index].getTeam();
		std::cout << "\nPlayer goals:" << allPlayers[index].getGoals();
		totalGoals += allPlayers[index].getGoals();
	}
	std::cout << "\nTotal goals: " << totalGoals;
}

void Ui::runUi()
{
	int command;
	while (true) {
		this->showMenu();
		command = this->inputCommand();
		try {
			switch (command) {
			case ADD_PLAYER: 
				this->addPlayer();
				break;
			case SHOW_IN_TEAM: 
				this->showAllInTeam();
				break;
			case SHOW_PLAYERS: 
				this->showAllPlayers();
				break;
			case EXIT: 
				std::cout << "\nYou left the app! Bye bye!";
				return;
			default:
				break;
			}
		}
		catch (std::exception& e) {
			std::cout << "\n Error: " << e.what() << "\n";
		}
	}
	return;
}
