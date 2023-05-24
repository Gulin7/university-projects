#include "dynamicArray.h"

DynamicArray* createDynamicArray(int capacity)
{
    DynamicArray* array = (DynamicArray*)malloc(sizeof(DynamicArray));

    if (array == NULL) {
        return NULL;
    }

    array->size = 0;

    array->capacity = capacity;

    array->elements = (TElem*)malloc(sizeof(TElem) * array->capacity);
    // Handling NULL/dangling pointers
    if (array->elements == NULL) {
        return NULL;
    }

    return array;
}

void destroyDynamicArray(DynamicArray* array)
{
    if (array == NULL) {
        return;
    }

    int i;
    for (i = 0; i < array->size; i++) {
        destroyMedicine(array->elements[i]);
    }

    free(array->elements);
    free(array);
}

void doubleCapacity(DynamicArray* array)
{
    DynamicArray* newArray = createArray(2 * array->capacity);

    newArray->size = array->size;

    for (int i = 0; i < newArray->size; i++) {
        newArray->elements[i] = array->elements[i];
    }

    destroyArray(array);

    array = newArray;

    destroyArray(newArray);
}

int getSizeArray(DynamicArray* array)
{
    return array->size;
}

void addToArray(DynamicArray* array, TElem element)
{
    if (array->size == array->capacity) {
        doubleCapacity(array);
    }

    array->elements[array->size] = element;
    array->size++;
}

void deleteFromArray(DynamicArray* array, int position)
{
    for (int index = position; index < array->size - 1; index++) {
        array->elements[index] = array->elements[index + 1];
    }

    destroyMedicine(array->elements[array->size - 1]);

    array->size--;
}

void update(DynamicArray* array, int position, TElem element)
{
    array->elements[position] = element;
}

int find(DynamicArray* array, TElem element)
{
    for (int index = 0; index < array->size; index++)
        if (*getName(array->elements[index]) == *getName(element) &&
            getConcentration(array->elements[index]) == getConcentration(element)) {
            return index;
        }
    return -1;
}
