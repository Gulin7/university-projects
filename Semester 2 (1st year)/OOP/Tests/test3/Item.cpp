#include "Item.h"

std::string Item::getCategory()
{
    return this->category;
}

std::string Item::getName()
{
    return this->name;
}

int Item::getQuantity()
{
    return this->quantity;
}

std::string Item::itemToString()
{
    std::string itemAsString = "Category: " + this->category + " | Name: " + this->name + " | Quantity: " + std::to_string(this->quantity);
    return itemAsString;
}
