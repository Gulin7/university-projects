#pragma once
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <algorithm>

using std::string;
using std::vector;
class Observer
{
public:
	virtual void update() = 0;
};
