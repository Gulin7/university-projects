//
// Created by Tudor on 14/03/2023.
//

#include "service.h"
#include <stdlib.h>

Service *createService(MedicineRepository *repository) {
    if (repository == NULL)
        return NULL;

    Service *service = (Service *) malloc(sizeof(Service));

    if (service == NULL)
        return NULL;

    service->repository = repository;

    return service;
}

void destroyService(Service *service) {
    if (service == NULL)
        return;

    destroyRepository(service->repository);
    free(service);
}

MedicineRepository *getRepository(Service *service) {
    return service->repository;
}

int addToService(Service *service, char *name, int concentration, int quantity, double price) {
    Medicine *medicineToAdd = createMedicine(name, concentration, quantity, price);
    int outcome = addToRepository(service->repository, medicineToAdd);
    return outcome;
}

int deleteFromService(Service *service, char *name, int concentration) {
    Medicine *outcome = deleteFromRepository(service->repository, name, concentration);
    if (outcome != NULL)
        return 1;
    return 0;
}

int updateInService(Service *service, char *name, int concentration, int newQuantity, double newPrice) {
    Medicine *medicineToUpdate = createMedicine(name, concentration, newQuantity, newPrice);
    Medicine *outcome = updateMedicineInRepository(service->repository, medicineToUpdate);
    if (outcome != NULL)
        return 1;
    return 0;
}

void sortMedicines(Service *service) {
    int lengthOfRepository = getSize(service->repository);
    for (int index1 = 0; index1 < lengthOfRepository - 1; index1++) {
        for (int index2 = index1 + 1; index2 < lengthOfRepository; index2++) {
            if (getName(service->repository->medicines->elements[index1]) >
                getName(service->repository->medicines->elements[index2])) {
                Medicine *auxiliaryMedicine = service->repository->medicines->elements[index1];
                service->repository->medicines->elements[index1] = service->repository->medicines->elements[index2];
                service->repository->medicines->elements[index2] = auxiliaryMedicine;
            }
        }
    }
}

void generateMedicines(Service *service) {
    Medicine *medicine1 = createMedicine("Paracetamol", 3, 5, 12);
    addToRepository(service->repository, copyMedicine(medicine1));
    destroyMedicine(medicine1);

    Medicine *medicine2 = createMedicine("Dexocalm", 8, 8, 25);
    addToRepository(service->repository, copyMedicine(medicine2));
    destroyMedicine(medicine2);

    Medicine *medicine3 = createMedicine("Claritin", 3, 21, 40);
    addToRepository(service->repository, copyMedicine(medicine3));
    destroyMedicine(medicine3);

    Medicine *medicine4 = createMedicine("Coldtusin", 3, 14, 25);
    addToRepository(service->repository, copyMedicine(medicine4));
    destroyMedicine(medicine4);

    Medicine *medicine5 = createMedicine("Nurofen", 3, 17, 8);
    addToRepository(service->repository, copyMedicine(medicine5));
    destroyMedicine(medicine5);

    Medicine *medicine6 = createMedicine("Magnevie", 3, 4, 30);
    addToRepository(service->repository, copyMedicine(medicine6));
    destroyMedicine(medicine6);

    Medicine *medicine7 = createMedicine("Trachisan", 3, 8, 10);
    addToRepository(service->repository, copyMedicine(medicine7));
    destroyMedicine(medicine7);

    Medicine *medicine8 = createMedicine("Detrical", 3, 4, 7);
    addToRepository(service->repository, copyMedicine(medicine8));
    destroyMedicine(medicine8);

    Medicine *medicine9 = createMedicine("Decasept", 3, 3, 5);
    addToRepository(service->repository, copyMedicine(medicine9));
    destroyMedicine(medicine9);

    Medicine *medicine10 = createMedicine("Fervex", 5, 22, 20);
    addToRepository(service->repository, copyMedicine(medicine10));
    destroyMedicine(medicine10);
}

MedicineRepository *filterByPrice(MedicineRepository *repository, double price) {
    if (repository == NULL)
        return NULL;

    MedicineRepository *newRepository = createRepository();

    for (int index = 0; index < getSize(repository); index++)
        if (getPrice(repository->medicines->elements[index]) <= price)
            addToRepository(newRepository, repository->medicines->elements[index]);

    return newRepository;
}