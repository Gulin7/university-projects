#include "User.h"

User::User(string name, string type) : name{ name }, type{ type }
{
}

string User::getName()
{
	return this->name;
}

string User::getType()
{
	return this->type;
}
