#pragma once

#include "repository.h"
#include "undoRedo.h"

/*
* 
*/
typedef struct {
	Repository* repo;
	OperationStack* undoStack;
	OperationStack* redoStack;
}Service;

/*
* 
*/
Service* createService(Repository* repo, OperationStack* undo, OperationStack* redo);

/*
* 
*/
void destroyService(Service* service);

/*
* 
*/
Repository* getRepository(Service* service);

/*
* 
*/
int addService(Service* service, char *name, int concentration, int quantity, double price);

/*
* 
*/
int deleteService(Service* service, char* name, int concentration);

/*
* 
*/
int updateService(Service* service, char* name, int concentration, int newQuantity, double newPrice);

/*
* 
*/
void sortService(Service* service);

/*
* 
*/
void generateMedicines(Service* service);

/*
* 
*/
int getServiceSize(Service* service);

/*
* 
*/
Repository* filterByPrice(Repository* repository, double price);

/*
* 
*/
int undo(Service* service);

/*
* 
*/
int redo(Service* service);