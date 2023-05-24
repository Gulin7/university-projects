#pragma once
#include "Player.h"
#include <vector>
#include <string>
#include <exception>

class Repository
{
private:
	std::vector<Player> players;
public:
	Repository(std::vector<Player> initialPlayers = {});

	void addPlayer(Player playerToAdd);
	void removePlayer(std::string name, std::string nationality);
	int findPlayer(std::string name, std::string nationality);

	std::vector<Player> getAllPlayers();
	std::vector<Player> getAllInTeam(std::string givenTeam);
};

