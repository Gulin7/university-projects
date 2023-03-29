//
// Created by gulin on 29/03/2023.
//

#ifndef A23_VOI_TRECE_PRIN_MONITOR_DYNAMIC_ARRAY_H
#define A23_VOI_TRECE_PRIN_MONITOR_DYNAMIC_ARRAY_H

#include "../domain/medicine.h"

typedef void *TElem;

/*
 *
 */
typedef struct {
    int size, capacity;
    TElem *elements;
} DynamicArray;

/*
 * Functions that creates a dynamicArray object and allocates memory for it and for its elements.
 */
DynamicArray *createArray(int capacity);

/*
 *
 */
void destroyArray(DynamicArray *array);

/*
 *
 */
void doubleCapacity(DynamicArray *array);

/*
 *
 */
int getSizeArray(DynamicArray *array);

/*
 *
 */
void addElement(DynamicArray *array, TElem element);

/*
 *
 */
void deleteAtPosition(DynamicArray *array, int position);

/*
 *
 */
void updateElement(DynamicArray *array, int position, TElem newElement);

/*
 *
 */
int findElement(DynamicArray *array, TElem element);

#endif //A23_VOI_TRECE_PRIN_MONITOR_DYNAMIC_ARRAY_H
