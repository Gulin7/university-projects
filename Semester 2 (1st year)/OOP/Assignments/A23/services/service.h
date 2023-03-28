//
// Created by Tudor on 14/03/2023.
//

#ifndef A23_GULIN7_SERVICE_H
#define A23_GULIN7_SERVICE_H
#define _CRT_SECURE_NO_WARNINGS

#include "../repository/repository.h"
#include "../operationStack/operation_stack.h"

/*
 * Struct that stores information about the service
 * */
typedef struct {
    MedicineRepository *repository;
    OperationStack *undoStack;
    OperationStack *redoStack;
} Service;

/*
 */
Service *createService(MedicineRepository *repository, OperationStack *undoStack, OperationStack *redoStack);

/*
 *
 */
void destroyService(Service *service);

/*
 *
 * */
MedicineRepository *getRepository(Service *service);

/*
*/
int addToService(Service *service, char *name, int concentration, int quantity, double price);

/*
 */
int deleteFromService(Service *service, char *name, int concentration);

/*
 */
int updateInService(Service *service, char *name, int concentration, int newQuantity, double newPrice);

/*
 */
void sortMedicines(Service *service);

/*
 * Function that generates 10 instances when starting the program.
 * :ctrl: pointer to Controller object
 * */
void generateMedicines(Service *service);

/*
 */

int getServiceSize(Service *service);

/*
 */
MedicineRepository *filterByPrice(MedicineRepository *repository, double price);

/*
 *
 */
int undoOperation(Service* service);

/*
 *
 */
int redoOperation(Service* service);

#endif //A23_GULIN7_SERVICE_H
