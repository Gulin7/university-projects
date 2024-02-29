#pragma once
#include "Repository.h"
#include "Song.h"
#include "PlayList.h"
#include <vector>
#include <exception>
#include <string>
#include <fstream>
#include <stack>

class Action
{
public:
	virtual void executeUndo() = 0;
	virtual void executeRedo() = 0;
};

