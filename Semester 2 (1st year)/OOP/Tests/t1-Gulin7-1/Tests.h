#pragma once
#include "Repository.h"
#include "Service.h"
#include <assert.h>
#include <exception>
#include <iostream>

class Tests
{
public:
	void testRepositoryAdd();
	void testServiceAdd();
	void testRepositoryGetByTeam();
	void testServiceGetByTeam();
	void testAll();
};

