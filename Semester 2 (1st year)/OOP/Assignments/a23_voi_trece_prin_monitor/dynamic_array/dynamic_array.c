//
// Created by gulin on 29/03/2023.
//

#include "dynamic_array.h"
#include <stdlib.h>

DynamicArray *createArray(int capacity) {
    DynamicArray *array = (DynamicArray *) malloc(sizeof(DynamicArray));

    if (array == NULL)
        return NULL;

    array->size = 0;
    array->capacity = capacity;
    array->elements = (TElem *) malloc(sizeof(TElem) * array->capacity);

    if (array->elements == NULL)
        return NULL;

    return array;
}

void destroyArray(DynamicArray *array) {
    if (array == NULL)
        return;

    for (int index = 0; index < array->size; index++) {
        destroyMedicine(array->elements[index]);
    }

    free(array->elements);
    free(array);
}

void doubleCapacity(DynamicArray *array) {
    DynamicArray *newArray = createArray(2 * array->capacity);

    newArray->size = array->size;

    for (int index = 0; index < newArray->size; index++)
        newArray->elements[index] = array->elements[index];

    destroyArray(array);
    array = newArray;
    destroyArray(newArray);
}

int getSizeArray(DynamicArray *array) {
    return array->size;
}

void addElement(DynamicArray *array, TElem element) {
    if (array->size == array->capacity)
        doubleCapacity(array);

    array->elements[array->size] = element;
    array->size++;

}

void deleteAtPosition(DynamicArray *array, int position) {
    for (int index = position; index < array->size - 1; index++)
        array->elements[index] = array->elements[index + 1];

    destroyMedicine(array->elements[array->size - 1]);

    array->size--;
}

void updateElement(DynamicArray *array, int position, TElem newElement) {
    array->elements[position] = newElement;
}

int findElement(DynamicArray *array, TElem element) {
    for (int index = 0; index < array->size; index++)
        if (*getName(array->elements[index]) == *getName(element) && getConcentration(array->elements[index]) ==
                                                                     getConcentration(element) &&
            getQuantity(array->elements[index]) == getQuantity(element) &&
            getPrice(array->elements[index]) == getPrice(element))
            return index;

    return -1;
}
