#pragma once

#include <stdlib.h>

typedef int TElem;

typedef struct
{
    TElem* operationsUndo;
    int undoCapacity;
    int undoSize;
    TElem* operationsRedo;
    int redoCapacity;
    int redoSize;

}Operations;

Operations* createOperations();

void addUndoOp(Operations* undoRedo, int operation);
void addRedoOp(Operations* undoRedo, int operation);

void deleteUndoOp(Operations* undoRedo);
void deleteRedoOp(Operations* undoRedo);

void destroyOperations(Operations* undoRedo);