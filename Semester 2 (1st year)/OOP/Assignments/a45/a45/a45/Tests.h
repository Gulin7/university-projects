#pragma once

#include "Event.h"
#include "DynamicVector.h"
#include "Repository.h"
#include "UserService.h"
#include "AdministratorService.h"

// EVENT
void testEvent();

// REPOSITORY
void testRepositoryAdd();

void testRepositoryRemove();

void testRepositoryUpdate();

// USER SERVICE
void testUserServiceAdd();

void testUserServiceRemove();

void testUserServiceGetByMonth();

// ADMINISTRATOR SERVICE
void testAdministratorServiceAdd();

void testAdministratorServiceRemove();

void testAdministratorServiceUpdate();

void testAdministratorServiceGenerators();

// ALL TESTS
void runAllTests();