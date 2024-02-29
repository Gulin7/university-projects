#pragma once

typedef int TElem;

typedef struct
{
	TElem* elems;
	int size, capacity;
}DynamicArray;

DynamicArray* createArray(int capacity);
void destroyArray(DynamicArray* arr);

int getCapacity(DynamicArray* arr);
int getSize(DynamicArray* arr);

void testDynamicArray();

void addElement(DynamicArray* arr, TElem elem);