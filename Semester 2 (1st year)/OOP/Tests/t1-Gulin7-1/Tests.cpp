#include "Tests.h"
#include <assert.h>
#include <exception>

void Tests::testRepositoryAdd()
{
	Player player1{ "Ana","ROU","Larvik",3 };
	Player player2{ "Mara","FRA","Larvik", 5 };
	std::vector<Player> initialPlayers = {};
	Repository repository{ initialPlayers };
	assert(repository.findPlayer(player1.getName(), player1.getNationality()) == -1);
	repository.addPlayer(player1);
	assert(repository.findPlayer(player1.getName(), player1.getNationality()) == 0);
	try {
		repository.addPlayer(player1);
	}
	catch (std::exception) {
		assert(true);
	}
}

void Tests::testServiceAdd()
{
	Player player1{ "Ana","ROU","Larvik",3 };
	Player player2{ "Mara","FRA","Larvik", 5 };
	std::vector<Player> initialPlayers = {};
	Repository repository{ initialPlayers };
	Service service{ repository };
	assert(service.findPlayer(player1.getName(), player1.getNationality()) == -1);
	service.addPlayer(player1);
	assert(service.findPlayer(player1.getName(), player1.getNationality()) == 0);
	try {
		service.addPlayer(player1);
	}
	catch (std::exception) {
		assert(true);
	}
}

void Tests::testRepositoryGetByTeam()
{
	Player player1{ "Ana","ROU","Larvik",3 };
	Player player2{ "Mara","FRA","Larvik", 5 };
	std::vector<Player> initialPlayers = {};
	Repository repository{ initialPlayers };
	repository.addPlayer(player2);
	repository.addPlayer(player1);
	std::vector<Player> players = repository.getAllInTeam("Larvik");
	assert(players.size() == 2);
	assert(players[0] == player2);
	assert(players[1] == player1);
}

void Tests::testServiceGetByTeam()
{
	Player player1{ "Ana","ROU","Larvik",3 };
	Player player2{ "Mara","FRA","Larvik", 5 };
	std::vector<Player> initialPlayers = {};
	Repository repository{ initialPlayers };
	Service service{ repository };
	service.addPlayer(player2);
	service.addPlayer(player1);
	std::vector<Player> players = service.getAllInTeam("Larvik");
	assert(players.size() == 2);
	assert(players[0] == player1);
}

void Tests::testAll()
{
	std::cout << "Tests started!";
	this->testRepositoryAdd();
	std::cout << "\nTest repo add good!";
	this->testRepositoryGetByTeam();
	std::cout << "\nTest repo get team good!";
	this->testServiceAdd();
	std::cout << "\nTest service add good!";
	this->testServiceGetByTeam();
	std::cout << "\nTest service get team good!";
	std::cout << "\nTests passed!\n";
}
