#include "UndoRedo.h"

undoRedoService* createUndoRedo()
{
    undoRedoService* undoRedo = (undoRedoService*)malloc(sizeof(undoRedoService));
    undoRedo->repositoryUndo = createRepository();
    undoRedo->repositoryRedo = createRepository();
    undoRedo->undoRedoOperations = createOperations();
    return undoRedo;
}

void addUndo(undoRedoService* undoRedo, char* name, int concentration, int quantity, float price, int operation)
{
    addMedicine(undoRedo->repositoryUndo, name, concentration, quantity, price);
    addUndoOp(undoRedo->undoRedoOperations, operation);
}

void addRedo(undoRedoService* undoRedo, char* name, int concentration, int quantity, float price, int operation)
{
    addMedicine(undoRedo->repositoryRedo, name, concentration, quantity, price);
    addRedoOp(undoRedo->undoRedoOperations, operation);
}

void deleteRedo(undoRedoService* undoRedo)
{
    destroyMedicines(undoRedo->repositoryRedo->medicines, undoRedo->repositoryRedo->size);
    undoRedo->repositoryRedo->size = 0;
    for (int index = 0; index < undoRedo->undoRedoOperations->redoSize; index++)
        deleteRedoOp(undoRedo->undoRedoOperations);
    undoRedo->undoRedoOperations->redoSize = 0;
}

void destroyUndoRedo(undoRedoService** undoRedo)
{
    destroyRepository(&(**undoRedo).repositoryRedo);
    destroyRepository(&(**undoRedo).repositoryUndo);
    destroyOperations((*undoRedo)->undoRedoOperations);
    undoRedo = NULL;
}
