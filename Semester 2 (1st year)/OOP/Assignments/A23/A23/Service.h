#pragma once

#include "Medicine.h"
#include "Repository.h"
#include "UndoRedo.h"


typedef struct
{
    Repository* repository;

    undoRedoService* undoRedo;
}Service;

Service* createService(Repository* repository);

void destroyService(Service** service);

int getMedicinesSize(Service* service);
Medicine* getMedicinesService(Service* service);

int undo(Service* service);
int redo(Service* service);

void deleteRedoService(Service* service);

int addMedicineService(Service* service, char* name, int concentration, int quantity, float price);

int updateMedicineService(Service* service, char* name, int concentration, int quantity, float price);

int deleteMedicineService(Service* service, char* name, int concentration);

void generateMedicines(Service* service);