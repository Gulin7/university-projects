#include "Service.h"
#include <algorithm>

bool compareGoals(Player& player1, Player& player2) {
	if (player1.getGoals() <= player2.getGoals())
		return true;
	return false;
}

Service::Service(Repository initialRepository)
{
	this->repository = initialRepository;
}

/*
* adds a player to the service
* it calls the function addPlayer in repository, which adds a player if it isnt already in the repo
* otherwise it throws an exception
*/
void Service::addPlayer(Player playerToAdd)
{
	this->repository.addPlayer(playerToAdd);
}

void Service::removePlayer(std::string name, std::string nationality)
{
	this->repository.removePlayer(name, nationality);
}

int Service::findPlayer(std::string name, std::string nationality)
{
	return this->repository.findPlayer(name, nationality);
}

std::vector<Player> Service::getAllPlayers()
{
	return this->repository.getAllPlayers();
}

/*
* it gets all players in the given team
* then it sorts the vector with depending on goals
*/
std::vector<Player> Service::getAllInTeam(std::string givenTeam)
{
	std::vector<Player> playersByGoals = this->repository.getAllInTeam(givenTeam);
	std::sort(playersByGoals.begin(), playersByGoals.end(), compareGoals);
	return playersByGoals;
}

void Service::generatePlayers()
{
	Player player1{"Ana","ROU","Larvik",3};
	Player player2{"Mara","FRA","Larvik", 5};
	Player player3{"Maria","NOR","HCM", 15};
	Player player4{"Alexia","SWE","Rostov-Don",30};
	Player player5{"Raluca","RUS","HCM",20};

	this->addPlayer(player1);
	this->addPlayer(player2);
	this->addPlayer(player3);
	this->addPlayer(player4);
	this->addPlayer(player5);
}
