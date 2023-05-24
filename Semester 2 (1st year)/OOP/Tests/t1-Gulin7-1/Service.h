#pragma once
#include "Repository.h"
#include <vector>
#include <string>
#include <exception>

class Service
{
private:
	Repository repository;
public:
	Service(Repository initialRepository);

	void addPlayer(Player playerToAdd);
	void removePlayer(std::string name, std::string nationality);
	int findPlayer(std::string name, std::string nationality);

	std::vector<Player> getAllPlayers();
	std::vector<Player> getAllInTeam(std::string givenTeam);

	void generatePlayers();
};
