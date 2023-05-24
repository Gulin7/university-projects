#include "Repository.h"
#include <exception>


Repository::Repository(std::vector<Player> initialPlayers)
{
	this->players = initialPlayers;
}

/* 
* REPOSITORY ADD
* Adds a player to the repository.
* If that player is already in the repository, it throws an exception.
*/
void Repository::addPlayer(Player playerToAdd)
{
	int position = this->findPlayer(playerToAdd.getName(), playerToAdd.getNationality());
	if (position!=-1)
		throw std::exception("Player already exists!");

	this->players.push_back(playerToAdd);
}

void Repository::removePlayer(std::string name, std::string nationality)
{
	int position = this->findPlayer(name, nationality);
	if (position == -1)
		throw std::exception("Player does not exist!");
	this->players.erase(this->players.begin() + position);
}

int Repository::findPlayer(std::string name, std::string nationality)
{
	for (int index = 0; index < this->players.size(); index++) {
		if (this->players[index].getName() == name && this->players[index].getNationality() == nationality)
			return index;
	}
	return -1;
}

std::vector<Player> Repository::getAllPlayers()
{
	return this->players;
}

/*
* givenTeam - the team whose players we are returning
* it returns all players in repository that are in the given team
*/
std::vector<Player> Repository::getAllInTeam(std::string givenTeam)
{
	std::vector<Player> playersInTeam = {};
	for (int index = 0; index < this->players.size(); index++)
		if (this->players[index].getTeam() == givenTeam)
			playersInTeam.push_back(this->players[index]);
	return playersInTeam;
}
