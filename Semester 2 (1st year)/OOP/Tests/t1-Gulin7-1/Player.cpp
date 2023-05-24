#include "Player.h"

Player::Player(std::string name, std::string nationality, std::string team, int numberOfGoals)
{
	this->name = name;
	this->nationality = nationality;
	this->team = team;
	this->numberOfGoals = numberOfGoals;
}

std::string Player::getName()
{
	return this->name;
}

std::string Player::getNationality()
{
	return this->nationality;
}

std::string Player::getTeam()
{
	return this->team;
}

int Player::getGoals()
{
	return this->numberOfGoals;
}

void Player::setName(std::string newName)
{
	this->name = newName;
}

void Player::setNationality(std::string newNationality)
{
	this->nationality = newNationality;
}

void Player::setTeam(std::string newTeam)
{
	this->team = newTeam;
}

void Player::setGoals(int newGoals)
{
	this->numberOfGoals = newGoals;
}

bool Player::operator==(Player& playerToCheck)
{
	if (this->name == playerToCheck.getName() && this->numberOfGoals == playerToCheck.getGoals() && this->nationality == playerToCheck.getNationality() && this->team == playerToCheck.getTeam())
		return true;
	return false;
}
