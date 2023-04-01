#pragma once

#include "medicine.h"
#include "dynamicArray.h"

/*
* 
*/
typedef struct {
	DynamicArray* medicines;
}Repository;

/*
* 
*/
Repository* createRepository();

/*
* 
*/
void destroyRepository(Repository *repo);

/*
* 
*/
int getSizeRepository(Repository* repo);

/*
* 
*/
int addRepository(Repository* repo, Medicine* medicine);

/*
* 
*/
Medicine* deleteRepository(Repository* repo, char *name, int concentration);

/*
* 
*/
Medicine* updateRepository(Repository* repo, Medicine* medicine);