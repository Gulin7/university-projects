//
// Created by gulin on 29/03/2023.
//

#include "service.h"
#include <string.h>

Service *createService(MedicineRepository *repository, OperationStack *undostack, OperationStack *redostack) {
    return NULL;
}

void destroyService(Service *service) {

}

MedicineRepository *getRepository(Service *service) {
    return NULL;
}

int addToService(Service *service, char *name, int concentration, int quantity, double price) {
    return 0;
}

int deleteFromService(Service *service, char *name, int concentration) {
    return 0;
}

int updateInService(Service *service, char *name, int concentration, int quantity, double price) {
    return 0;
}

void sortMedicines(Service *service) {

}

int getServiceSize(Service *service) {
    return 0;
}

MedicineRepository *filterByPrice(MedicineRepository *repository, double price) {
    return NULL;
}

int undoOperation() {
    return 0;
}

int redoOperation() {
    return 0;
}
