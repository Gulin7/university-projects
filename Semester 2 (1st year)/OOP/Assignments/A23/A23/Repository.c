#include "Repository.h"
#include <stdio.h>
#include <stdlib.h>

Repository* createRepository()
{
    Repository* repository = (Repository*)malloc(sizeof(Repository));
    if (repository == NULL)
        return repository;
    
    repository->capacity = 10;
    repository->size = 0;
    repository->medicines = (Medicine*)malloc(repository->capacity * sizeof(Medicine));

    return repository;
}

void destroyRepository(Repository** repository)
{
    for (int index = (*repository)->size - 1; index >= 0; index--)
    {
        destroyMedicine((*repository)->medicines[index]);
    }
    free((*repository)->medicines);
    free(*repository);
}

Medicine* getMedicines(Repository* repository)
{
    return repository->medicines;
}

void setMedicines(Repository* repository, Medicine* medicineList)
{
    repository->medicines = medicineList;
}

int getSizeRepository(Repository* repository)
{
    return repository->size;
}

int findMedicine(Repository* repository, char* name, int concentration)
{
    for (int index = 0; index < repository->size; index++)
        if (strcmp(getName(repository->medicines[index]), name) == 0 && getConcentration(repository->medicines[index]) == concentration)
            return index;
    return -1;
}

int findMedicineByName(Repository* repository, char* name)
{
    return 0;
}

void addMedicine(Repository* repository, char* name, int concentration, int quantity, float price)
{
    Medicine medicine = createMedicine(name, concentration, quantity, price);
    if (repository->size == repository->capacity) {
        repository->capacity *= 2;
        repository->medicines = (Medicine*)realloc(repository->medicines, repository->capacity * sizeof(Medicine));
    }
    repository->size++;
    repository->medicines[repository->size] = copyMedicine(medicine);
    destroyMedicine(medicine);
}

void deleteMedicine(Repository* repository, char* name, int concentration)
{
    int position = findMedicine(repository, name, concentration);
    if (position == -1)
        return;
    repository->size--;
    for (int index = position; index < repository->size; index++)
        repository->medicines[index] = repository->medicines[index + 1];
}

void destroyMedicines(Medicine* medicines, int size)
{
    for (int index = 0; index < size; index++)
        free(medicines[index].name);
    free(medicines);
}

void updateMedicine(Repository* repository, char* name, int concentration, int newQuantity, float newPrice)
{
    int position = findMedicine(repository, name, concentration);
    if ( position == -1)
        return;
    setQuantity(&((Medicine*)repository->medicines)[position], newQuantity);
    setPrice(&((Medicine*)repository->medicines)[position], newPrice);

}

void sortMedicinesByName(Repository* repository)
{
    Medicine* sortedMedicines = repository->medicines;
    for(int firstIndex = 0; firstIndex<repository->size-1;firstIndex++)
        for(int second = firstIndex+1;second<repository->size;second++)
            if (strcmp(getName(sortedMedicines[firstIndex]), getName(sortedMedicines[second])) > 0)
            {
                Medicine swapMedicine = copyMedicine(sortedMedicines[firstIndex]);
                sortedMedicines[firstIndex] = copyMedicine(sortedMedicines[second]);
                sortedMedicines[second] = copyMedicine(swapMedicine);
            }
    repository->medicines = sortedMedicines;
}
