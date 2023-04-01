#pragma once

#include "medicine.h"

typedef void* TElem;

/*
* 
*/
typedef struct {
	int size;
	int capacity;
	TElem* elements;
} DynamicArray;

/*
* 
*/
DynamicArray* createDynamicArray();

/*
* 
*/
void destroyDynamicArray(DynamicArray* array);

/*
* 
*/
void doubleCapacity(DynamicArray* array);

/*
* 
*/
int getSizeArray(DynamicArray* array);

/*
* 
*/
void addToArray(DynamicArray* array, TElem element);

/*
* 
*/
void deleteFromArray(DynamicArray* array, int position);

/*
* 
*/
void update(DynamicArray* array, int position, TElem element);

/*
* 
*/
int find(DynamicArray* array, TElem element);

