//
// Created by gulin on 29/03/2023.
//

#include "repository.h"

MedicineRepository *createRepository() {
    MedicineRepository *repo = (MedicineRepository *) malloc(sizeof(MedicineRepository));

    if (repo == NULL)
        return NULL;

    repo->medicines = createArray(100);
    return repo;

}

void destroyRepository(MedicineRepository *repo) {
    if (repo == NULL)
        return;

    destroyArray(repo->medicines);
    free(repo);
}

int getSize(MedicineRepository *repo) {
    if (repo == NULL)
        return -1;
    return getSizeArray(repo->medicines);
}

int addToRepository(MedicineRepository *repo, Medicine *medicine) {
    if(repo == NULL || medicine == NULL)
        return 0;

    int position = findElement(repo->medicines, medicine);
    if(position != -1){
        updateRepository(repo, medicine);
    }
    else {
        addElement(repo->medicines, medicine);
        return 1;
    }
    return 0;
}

Medicine *deleteFromRepository(MedicineRepository *repo, char *name, int concentration) {
    if( repo == NULL || name == NULL)
        return NULL;

    Medicine *medicine = createMedicine(name, concentration,0,0);

    int position = findElement(repo->medicines, medicine);

    if(position!=-1){
        deleteAtPosition(repo->medicines, position);
        return repo->medicines->elements[position];
    }

    return NULL;
}

Medicine *updateRepository(MedicineRepository *repo, Medicine *medicine) {
    if(repo == NULL || medicine == NULL)
        return NULL;

    int position = findElement(repo->medicines, medicine);
    if(position==-1)
        return NULL;

    updateElement(repo->medicines, position, medicine);
    return medicine;
}
