#include "DynamicArray.h"
#include <stdlib.h>
#include <assert.h>

DynamicArray* createArray(int capacity)
{
	DynamicArray* arr = malloc(sizeof(DynamicArray) * capacity);
	if (arr == NULL)
		return NULL;

	arr->capacity = capacity;
	arr->size = 0;
	arr->elems = malloc(capacity * sizeof(TElem));
	if (arr->elems == NULL)
		return NULL;
}

void destroyArray(DynamicArray* arr)
{
	if (arr == NULL)
		return;
	free(arr->elems);
	free(arr);

}

int getCapacity(DynamicArray* arr)
{
	return arr->capacity;
}

int getSize(DynamicArray* arr)
{
	return arr->size;
}

void testDynamicArray()
{
	DynamicArray* arr = createArray(2);
	assert(getCapacity(arr) == 2);
	assert(getSize(arr) == 0);

	addElement(arr, 10);
	assert(getCapacity(arr) == 2);
	assert(getSize(arr) == 1);

	addElement(arr, 15);
	assert(getCapacity(arr) == 2);
	assert(getSize(arr) == 2);

	addElement(arr, 69);
	assert(getCapacity(arr) == 4);
	assert(getSize(arr) == 3);

}

void resizeDynamicArray(DynamicArray* arr) {
	if (arr == NULL)
		return;
	arr->capacity *= 2;
	TElem* aux=realloc(arr->elems, arr->capacity*sizeof(TElem));
	if (aux == NULL) {
		arr->capacity /= 2;
		return;
	}
	arr->elems = aux;

}

void addElement(DynamicArray* arr, TElem elem)
{
	if (arr == NULL)
		return;
	
	if (arr->size == arr->capacity)
		resizeDyanmicArray(arr);
	arr->elems[arr->size] = elem;
}
