#include "UserRepository.h"

#include <algorithm>
#include <exception>
#include <fstream>

using std::ifstream;

void UserRepository::readFile()
{
	ifstream inputFile{ this->filePath };

	if (!inputFile.is_open())
	{
		throw std::exception{ "Failed to open file!" };
	}

	string currentUser;

	while (getline(inputFile, currentUser))
	{
		User userToAdd{ currentUser };
		this->addUser(userToAdd);
	}

	inputFile.close();
}

int UserRepository::findUser(string userName)
{
	auto position = find_if(
		this->usersDatabase.begin(),
		this->usersDatabase.end(),
		[userName](User currentUser)
		{
			return currentUser.getName() == userName;
		});

	if (position == this->usersDatabase.end())
		return -1;

	return position - this->usersDatabase.begin();
}

void UserRepository::addUser(User userToAdd)
{
	if (this->findUser(userToAdd.getName()) != -1)
		throw std::exception{ "User already in repository!" };

	usersDatabase.push_back(userToAdd);
}

vector<User>& UserRepository::getAll()
{
	return this->usersDatabase;
}
