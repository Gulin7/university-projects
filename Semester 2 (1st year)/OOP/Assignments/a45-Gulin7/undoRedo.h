#pragma once

#include "dynamicArray.h"

/*
* 
*/
typedef struct {
	Medicine* medicine;
	char* type;
}Operation;

/*
* 
*/
typedef struct {
	DynamicArray* operations;
}OperationStack;

/*
* 
*/
Operation* createOperation(Medicine* medicine, char* type);

/*
* 
*/
Medicine* getOperationMedicine(Operation* operation);

/*
* 
*/
OperationStack* createOperationStack();

/*
* 
*/
void destroyOperationStack(OperationStack* stack);

/*
* 
*/
void pushOperation(OperationStack* stack, Operation* operation);

/*
* 
*/
Operation* popOperation(OperationStack* stack);
