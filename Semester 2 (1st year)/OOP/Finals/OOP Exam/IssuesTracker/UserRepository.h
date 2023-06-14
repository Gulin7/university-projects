#pragma once

#include <vector>

#include "User.h"

using std::vector;

class UserRepository
{
private:
	vector<User> users;

	string filePath;

public:
	UserRepository(string filePath);

	void readFile();

	int findPosition(string userName);

	User& getUserAtPosition(int position);
	void add(User userToAdd);
	
	vector<User>& getAll();
};

