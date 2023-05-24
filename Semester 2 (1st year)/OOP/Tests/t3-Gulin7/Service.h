#pragma once
#include "Item.h"
#include <vector>
#include <fstream>
#include <sstream>

class Service
{
private:
	std::vector<Item> items;
	std::string filename;
public:
	Service(std::string filename, std::vector<Item> items={}): filename(filename), items(items){}
	std::vector<Item> getAllItems();
	std::vector<Item> getAllItemsCategory(std::string category);

	void readFromFile();
};

