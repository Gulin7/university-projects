#pragma once
#include <string>
class Item
{
private:
	std::string category;
	std::string name;
	int quantity;
public:
	Item(std::string category, std::string name, int quantity): category(category), name(name), quantity(quantity){}
	std::string getCategory();
	std::string getName();
	int getQuantity();

	std::string itemToString();
};

