#include "UserRepository.h"
#include "StringOperations.h"

#include <fstream>
#include <algorithm>

UserRepository::UserRepository(string filePath) : filePath { filePath }
{
	this->readFile();
}

void UserRepository::readFile()
{
	std::ifstream inputFile{ this->filePath };

	if (!inputFile.is_open())
		throw std::exception{ "Cannot open file to read!" };

	string currentUser;

	while (getline(inputFile, currentUser))
	{
		vector<string> fields = splitString(currentUser, '|');

		if (fields.size() != 2)
			continue;

		User userToAdd{ fields[0], fields[1] };
		users.push_back(userToAdd);
	}

	inputFile.close();
}

int UserRepository::findPosition(string userName)
{
	auto position = std::find_if(users.begin(), users.end(),
		[&userName](User currentUser)
		{
			return currentUser.getName() == userName;
		});

	if (position == users.end()) return -1;

	return position - users.begin();
}

User& UserRepository::getUserAtPosition(int position)
{
	if (position < 0 || position >= users.size())
		throw std::runtime_error{ "Index out of range!" };

	return users[position];
}

void UserRepository::add(User userToAdd)
{
	if (this->findPosition(userToAdd.getName()) != -1)
		throw std::exception{ "User already in repository!" };

	users.push_back(userToAdd);
}

vector<User>& UserRepository::getAll()
{
	return users;
}
