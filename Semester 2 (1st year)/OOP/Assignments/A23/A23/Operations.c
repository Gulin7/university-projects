#include "Operations.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

Operations* createOperations()
{
    Operations* undoRedo = (Operations*)malloc(sizeof(Operations));
    undoRedo->operationsUndo = (TElem*)malloc(sizeof(TElem));
    undoRedo->operationsRedo = (TElem*)malloc(sizeof(TElem));
    undoRedo->undoCapacity = 10;
    undoRedo->redoCapacity = 10;
    undoRedo->undoSize = 0;
    undoRedo->redoSize = 0;
    return undoRedo;
}

void addUndoOp(Operations* undoRedo, int operation)
{
    if (undoRedo->undoSize == undoRedo->undoCapacity) {
        undoRedo->undoCapacity *= 2;
        undoRedo->operationsUndo = (TElem*)realloc(undoRedo->operationsUndo, undoRedo->undoCapacity * sizeof(TElem));
    }
    undoRedo->operationsUndo[undoRedo->undoSize++] = operation;
}

void addRedoOp(Operations* undoRedo, int operation)
{
    if (undoRedo->redoSize == undoRedo->redoCapacity) {
        undoRedo->redoCapacity *= 2;
        undoRedo->operationsRedo = (TElem*)realloc(undoRedo->operationsRedo, undoRedo->redoCapacity * sizeof(TElem));
    }
    undoRedo->operationsRedo[undoRedo->redoSize++] = operation;
}

void deleteUndoOp(Operations* undoRedo)
{
    undoRedo->undoSize--;
    undoRedo->operationsUndo[undoRedo->undoSize] = NULL;
}

void deleteRedoOp(Operations* undoRedo)
{
    undoRedo->redoSize--;
    undoRedo->operationsRedo[undoRedo->redoSize] = NULL;
}

void destroyOperations(Operations* undoRedo)
{
    free(undoRedo->operationsUndo);
    free(undoRedo->operationsRedo);
    undoRedo = NULL;
}
