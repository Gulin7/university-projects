#pragma once

#include "User.h"

#include <vector>

using std::vector;

class UserRepository
{
private:
	vector<User> usersDatabase;
	string filePath;

public:
	UserRepository(string filePath) : filePath{ filePath } 
	{
		this->readFile();
	}

	void readFile();

	int findUser(string userName);

	void addUser(User userToAdd);
	vector<User>& getAll();
};

