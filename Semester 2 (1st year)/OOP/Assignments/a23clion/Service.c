#include "Service.h"

Service* createService(Repository* repository)
{
    Service* service = (Service*)malloc(sizeof(Service));
    if (service == NULL)
        return NULL;
    service->repository = repository;
    service->undoRedo = createUndoRedo();
    return service;
}

void destroyService(Service** service)
{
    destroyRepository(&(**service).repository);
    destroyUndoRedo(&(**service).undoRedo);
    free(*service);
    *service = NULL;
}

int getMedicinesSize(Service* service)
{
    return getSizeRepository(service->repository);
}

Medicine* getMedicinesService(Service* service)
{
    return getMedicines(service->repository);
}

int undo(Service* service)
{
    // IF WE HAVE NO OPERATIONS LEFT TO UNDO
    if (service->undoRedo->repositoryUndo->size == 0)
        return -1;
    int size = service->undoRedo->repositoryUndo->size - 1;
    char* name = service->undoRedo->repositoryUndo->medicines[size].name;
    int concentration = service->undoRedo->repositoryUndo->medicines[size].concentration;
    int quantity = service->undoRedo->repositoryUndo->medicines[size].quantity;
    float price = service->undoRedo->repositoryUndo->medicines[size].price;

    int lastPerformedOperation = service->undoRedo->undoRedoOperations->operationsUndo[service->undoRedo->undoRedoOperations->undoSize - 1];


    if (lastPerformedOperation == 1) {
        deleteMedicineService(service, name, concentration);
        addRedo(service->undoRedo, name, concentration, quantity, price, 2);
    }
    else if (lastPerformedOperation == 2) {
        addMedicineService(service, name, concentration, quantity, price);
        lastPerformedOperation = 1;
        addRedo(service->undoRedo, name, concentration, quantity, price, 1);
    }
    else if (lastPerformedOperation==3){
        int position = findMedicine(service->repository, name, concentration);
        int newQuantity = service->repository->medicines[position].quantity;
        float newPrice = service->repository->medicines[position].price;
        updateMedicineService(service, name, concentration, quantity, price);
        addRedo(service->undoRedo, name, concentration, newQuantity, newPrice, 3);
    }

    deleteMedicine(service->undoRedo->repositoryUndo, name, concentration);
    deleteUndoOp(service->undoRedo->undoRedoOperations);

    return 0;

}

int redo(Service* service)
{
    if (service->undoRedo->repositoryRedo->size == 0)
        return -1;

    int size = service->undoRedo->repositoryRedo->size - 1;

    char* name = service->undoRedo->repositoryRedo->medicines[size].name;
    int concentration = service->undoRedo->repositoryRedo->medicines[size].concentration;
    int quantity = service->undoRedo->repositoryRedo->medicines[size].quantity;
    float price = service->undoRedo->repositoryRedo->medicines[size].price;

    int lastPerformedOperation = service->undoRedo->undoRedoOperations->operationsRedo[service->undoRedo->undoRedoOperations->redoSize - 1];


    if (lastPerformedOperation == 1) {
        deleteMedicineService(service, name, concentration);
        addUndo(service->undoRedo, name, concentration, quantity, price, 2);
    }
    else if (lastPerformedOperation == 2) {
        addMedicineService(service, name, concentration, quantity, price);
        addUndo(service->undoRedo, name, concentration, quantity, price, 1);
    }
    else {
        int position = findMedicine(service->repository, name, concentration);
        int newQuantity = service->repository->medicines[position].quantity;
        float newPrice = service->repository->medicines[position].price;
        updateMedicineService(service, name, concentration, quantity, price);
        addUndo(service->undoRedo, name, concentration, newQuantity, newPrice, 3);
    }

    deleteMedicine(service->undoRedo->repositoryUndo, name, concentration);
    deleteRedoOp(service->undoRedo->undoRedoOperations);

    return 0;
}

void deleteRedoService(Service* service)
{
    if (service->undoRedo->repositoryRedo->size == 0)
        return;
    deleteRedo(service->undoRedo);
}

int addMedicineService(Service* service, char* name, int concentration, int quantity, float price)
{
    if (findMedicine(service->repository, name, concentration) == -1)
        return -1;
    addMedicine(service->repository, name, concentration, quantity, price);
    return 0;
}

int updateMedicineService(Service* service, char* name, int concentration, int quantity, float price)
{
    int position = findMedicine(service->repository, name, concentration);
    if (position == -1)
        return -1;
    updateMedicine(service->repository, name, concentration, quantity, price);
    return 0;
}

int deleteMedicineService(Service* service, char* name, int concentration)
{
    int position = findMedicine(service->repository, name, concentration);
    if (position == -1)
        return -1;
    deleteMedicine(service->repository, name, concentration);
    return 0;
}

void generateMedicines(Service* service)
{
    addMedicineService(service, "Decasept",1,2,3);
    addMedicineService(service, "Trachisan",2,3,4);
    addMedicineService(service, "Paracetamol",3,4,5);
    addMedicineService(service, "Nurofen",5,10,20);
    addMedicineService(service, "Algocalmin",30, 5, 15);
    addMedicineService(service, "Fervex",20, 50, 10);
    addMedicineService(service, "Medi", 5, 100, 1);
    addMedicineService(service, "VitaminaC", 1000, 500, 2);
    addMedicineService(service, "Centrum", 100, 30, 2);
    addMedicineService(service, "Molekin", 1000, 20, 30);
}
