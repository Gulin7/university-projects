//
// Created by gulin on 29/03/2023.
//

#ifndef A23_VOI_TRECE_PRIN_MONITOR_SERVICE_H
#define A23_VOI_TRECE_PRIN_MONITOR_SERVICE_H

#include "../repository/repository.h"
#include "../undo_redo/undo_redo.h"

/*
 *
 */
typedef struct {
    MedicineRepository *repository;
    OperationStack *undoStack;
    OperationStack *redoStack;
} Service;

/*
 *
 */
Service *createService(MedicineRepository *repository, OperationStack *undostack, OperationStack *redostack);

/*
 *
 */
void destroyService(Service *service);

/*
 *
 */
MedicineRepository *getRepository(Service *service);

/*
 *
 */
int addToService(Service *service, char *name, int concentration, int quantity, double price);

/*
 *
 */
int deleteFromService(Service *service, char *name, int concentration);

/*
 *
 */
int updateInService(Service *service, char *name, int concentration, int quantity, double price);

/*
 *
 */
void sortMedicines(Service *service);

/*
 *
 */
int getServiceSize(Service *service);

/*
 *
 */
MedicineRepository *filterByPrice(MedicineRepository *repository, double price);

/*
 *
 */
int undoOperation();

/*
 *
 */
int redoOperation();


#endif //A23_VOI_TRECE_PRIN_MONITOR_SERVICE_H
