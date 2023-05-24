//
// Created by Tudor on 14/03/2023.
//

#include "repository.h"
#include <stdlib.h>

MedicineRepository *createRepository() {
    MedicineRepository *repository = (MedicineRepository *) malloc(sizeof(MedicineRepository));
    if (repository == NULL) {
        return NULL;
    }

    repository->medicines = createArray(20);

    return repository;
}

void destroyRepository(MedicineRepository *repository) {
    if (repository == NULL) {
        return;
    }
    destroyArray(repository->medicines);
    free(repository);
}

int getSize(MedicineRepository *repository) {
    if (repository == NULL) {
        return -1;
    }
    return getSizeArray(repository->medicines);
}

int addToRepository(MedicineRepository *repository, Medicine *medicine) {
    if (repository == NULL || medicine == NULL) {
        return 0;
    }

    int position = findElementInArray(repository->medicines, medicine);
    if (position != -1) {
        updateMedicineInRepository(repository, medicine);
    } else {
        addNewElement(repository->medicines, medicine);
        return 1;
    }
    return 0;
}

Medicine *deleteFromRepository(MedicineRepository *repository, char *name, int concentration) {
    if (repository == NULL || name == NULL) {
        return NULL;
    }

    Medicine *medicine = createMedicine(name, concentration, 0, 0);

    int position = findElementInArray(repository->medicines, medicine);

    if (position != -1) {
        deleteAtGivenPosition(repository->medicines, position);
        return 0;
    }
    return NULL;
}

Medicine *updateMedicineInRepository(MedicineRepository *repository, Medicine *medicine) {
    if (repository == NULL || medicine == NULL) {
        return NULL;
    }
    int position = findElementInArray(repository->medicines, medicine);
    if (position == -1)
        return NULL;
    updateArray(repository->medicines, position, medicine);
    return medicine;
}