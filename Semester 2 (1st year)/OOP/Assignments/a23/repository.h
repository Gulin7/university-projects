//
// Created by Tudor on 14/03/2023.
//

#ifndef A23_GULIN7_REPOSITORY_H
#define A23_GULIN7_REPOSITORY_H


#include "../domain/domain.h"
#include "../dynamicArray/dynamicArray.h"

/*
 * Struct that stores the Repository.
 */
typedef struct {
    DynamicArray *medicines;
} MedicineRepository;

/*
 *
 *
 * */
MedicineRepository *createRepository();

/*
 *
 *
 * */
void destroyRepository(MedicineRepository *repository);

/*
 * Getter for the size field of the OfferRepo struct
 * :repo: pointer to an OfferRepo object
 * return: int
 * */
int getSize(MedicineRepository *repository);

/*
 *
 *
 *
 *
 * */
int addToRepository(MedicineRepository *repository, Medicine *medicine);

/*
 * Function that implements the delete functionality using .delete() from DynamicArray.h.
 * :repo: pointer to an OfferRepo object
 * :destination: pointer to char
 * :departureDate: Date variable
 * return: pointer to Offer object
 * */
Medicine *deleteFromRepository(MedicineRepository *repo, char *name, int concentration);

/*
 *
 *
 *
 *
 * */
Medicine *updateMedicineInRepository(MedicineRepository *repository, Medicine *medicine);

#endif //A23_GULIN7_REPOSITORY_H