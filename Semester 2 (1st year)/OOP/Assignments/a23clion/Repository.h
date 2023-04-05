#pragma once
#include "Medicine.h"

typedef struct {
    Medicine* medicines;
    int size;
    int capacity;
}Repository;

Repository* createRepository();

void destroyRepository(Repository** repository);

Medicine* getMedicines(Repository* repository);
void setMedicines(Repository* repository, Medicine* medicineList);
int getSizeRepository(Repository* repository);

int findMedicine(Repository* repository, char* name, int concentration);
int findMedicineByName(Repository* repository, char* name);

void addMedicine(Repository* repository, char* name, int concentration, int quantity, float price);
void deleteMedicine(Repository* repository, char* name, int concentration);
void destroyMedicines(Medicine* medicines, int size);
void updateMedicine(Repository* repository, char* name, int concentration, int newQuantity, float newPrice);

void sortMedicinesByName(Repository* repository);
 