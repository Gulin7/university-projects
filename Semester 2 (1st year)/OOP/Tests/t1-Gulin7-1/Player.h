#pragma once
#include <string>

class Player
{
private:
	std::string name;
	std::string nationality;
	std::string team;
	int numberOfGoals;
public:
	Player() : name(""), nationality(""), team(""), numberOfGoals(0){}
	Player(std::string name, std::string nationality, std::string team, int numberOfGoals);
	
	std::string getName();
	std::string getNationality();
	std::string getTeam();
	int getGoals();

	void setName(std::string newName);
	void setNationality(std::string newNationality);
	void setTeam(std::string newTeam);
	void setGoals(int newGoals);

	bool operator==(Player& playerToCheck);
};

