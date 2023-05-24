#include "Service.h"
#include <algorithm>

bool sortCategoryName(Item item1, Item item2) {
    if (item1.getCategory() < item2.getCategory())
        return true;
    else if (item1.getCategory() > item2.getCategory())
        return false;
    else if (item1.getName() < item2.getName())
        return true;
    else
        return false;
}

bool sortQuantity(Item item1, Item item2) {
    if (item1.getQuantity() < item2.getQuantity())
        return true;
    else
        return false;
}

std::vector<Item> Service::getAllItems()
{
    std::vector<Item> allItems = this->items;
    std::sort(allItems.begin(), allItems.end(), sortCategoryName);
    return allItems;
}

std::vector<Item> Service::getAllItemsCategory(std::string category)
{
    std::vector<Item> allItemsCategory = {};
    for (auto& item : this->items) {
        if (item.getCategory() == category)
            allItemsCategory.push_back(item);
    }
    std::sort(allItemsCategory.begin(), allItemsCategory.end(), sortQuantity);
    return allItemsCategory;
}

void Service::readFromFile()
{
    std::ifstream inputFile(this->filename);
    std::string line;
    while (getline(inputFile, line)) {
        std::string token;
        std::stringstream ss(line);
        std::vector<std::string> data;
        while (getline(ss, token, ';')) {
            data.push_back(token);
        }
        Item newItem(data[0], data[1], stoi(data[2]));
        this->items.push_back((newItem));
    }
}
