#pragma once
#include <vector>
#include <string>
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

