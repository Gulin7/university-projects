#pragma once

#include "Repository.h"
#include "Operations.h"
#include "Medicine.h"
#include <stdlib.h>

typedef struct
{
    Operations* undoRedoOperations;
    Repository* repositoryUndo;
    Repository* repositoryRedo;

}undoRedoService;

undoRedoService* createUndoRedo();

void addUndo(undoRedoService* undoRedo, char* name, int concentration, int quantity, float price, int operation);
void addRedo(undoRedoService* undoRedo, char* name, int concentration, int quantity,int price, int operation);

void deleteRedo(undoRedoService* undoRedo);

void destroyUndoRedo(undoRedoService** undoRedo);
