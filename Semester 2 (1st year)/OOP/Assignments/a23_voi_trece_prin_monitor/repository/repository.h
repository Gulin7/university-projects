//
// Created by gulin on 29/03/2023.
//

#ifndef A23_VOI_TRECE_PRIN_MONITOR_REPOSITORY_H
#define A23_VOI_TRECE_PRIN_MONITOR_REPOSITORY_H

#include "../domain/medicine.h"
#include "../dynamic_array/dynamic_array.h"

/*
 * Struct - the repository.
 */
typedef struct {
    DynamicArray *medicines;
} MedicineRepository;

/*
 *
 */
MedicineRepository *createRepository();

/*
 * Function that destroys a repository and deallocates
 */
void destroyRepository(MedicineRepository *repo);

/*
 * Function that returns the size of the repository.
 * return: int
 */
int getSize(MedicineRepository *repo);

/*
 * Function that adds a medicine to the repository.
 * repo: pointer to a MedicineRepository
 * medicine: pointer to the medicine to be added
 *
 */
int addToRepository(MedicineRepository *repo, Medicine *medicine);

/*
 * Functions that deletes a medicine from the repository.
 */
Medicine *deleteFromRepository(MedicineRepository *repo, char *name, int concentration);

/*
 * Function that updates the repository.
 * repo: pointer to a MedicineRepository
 * medicine: pointer to a Medicine; we will update the medicine with the same name/concentration as this
 */
Medicine *updateRepository(MedicineRepository *repo, Medicine *medicine);

#endif //A23_VOI_TRECE_PRIN_MONITOR_REPOSITORY_H
