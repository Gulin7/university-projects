#pragma once
#include "Event.h"
#include "Repository.h"
#include "UserService.h"
#include "AdministratorService.h"
#include <vector>
#include <string>
#include <assert.h>

class UnitTests
{
public:
	UnitTests(){};
	void testServiceAdd();
	void testServiceRemove();
	void testGetByTitle();
	void runAllTests();
};

