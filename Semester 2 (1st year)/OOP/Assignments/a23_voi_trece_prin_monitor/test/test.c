//
// Created by gulin on 29/03/2023.
//

#include "test.h"
#include <assert.h>

#include "../domain/medicine.h"
#include "../repository/repository.h"
#include "../service/service.h"

void testDomain() {
    Medicine *medicine = createMedicine("Paracetamol", 5, 69, 4.20);
    assert(medicine != NULL);

    assert(getConcentration(medicine) == 5);
    assert(getPrice(medicine) == 4.20);
    assert(getQuantity(medicine) == 69);

    // test copy

    Medicine *newMedicine = copyMedicine(medicine);

    assert(getConcentration(medicine) == getConcentration(newMedicine));
    assert(getQuantity(medicine) == getQuantity(newMedicine));
    assert(getPrice(medicine) == getPrice(newMedicine));

    destroyMedicine(medicine);
    destroyMedicine(newMedicine);
}

void testDynamicArray() {
    DynamicArray *dynamicArray = createArray(100);

    assert(dynamicArray != NULL);

    assert(dynamicArray->capacity == 100);

    destroyArray(dynamicArray);
}

void testRepository() {
    MedicineRepository *repository = createRepository();
    Medicine *medicine = createMedicine("Paracetamol", 5, 69, 4.20);
    assert(repository != NULL);
    // TESTING THE ADD
    addToRepository(repository, medicine);
    assert(repository->medicines->elements[getSize(repository) - 1] == medicine);
    // TESTING THE DELETE
    deleteFromRepository(repository, getName(medicine), getConcentration(medicine));
    assert(getSize(repository) == 0);
    // TESTING UPDATE
    Medicine *newMedicine = createMedicine("Paracetamol", 5, 420, 6.9);
    addToRepository(repository, medicine);
    *updateMedicineInRepository(repository, newMedicine);
    assert(repository->medicines->elements[getSize(repository) - 1] == newMedicine);

    destroyMedicine(medicine);
    destroyMedicine(newMedicine);
    destroyRepository(repository);
}

void testService() {

    MedicineRepository *repository = createRepository();
    OperationStack *undoStack = createOperationStack();
    OperationStack *redoStack = createOperationStack();
    Service *service = createService(repository, undoStack, redoStack);
    assert(service != NULL);
    // TESTING ADD
    Medicine *medicine = createMedicine("Algocalmin", 20, 3, 5);
    addToService(service, getName(medicine), getConcentration(medicine), getQuantity(medicine), getPrice(medicine));
    assert(getServiceSize(service) == 1);
    assert(*getName(service->repository->medicines->elements[0]) == *getName(medicine));
    assert(getConcentration(service->repository->medicines->elements[0]) == getConcentration(medicine));
    assert(getQuantity(service->repository->medicines->elements[0]) == getQuantity(medicine));
    assert(getPrice(service->repository->medicines->elements[0]) == getPrice(medicine));

    // TEST DELETE
    deleteFromService(service, getName(medicine), getConcentration(medicine));
    assert(getServiceSize(service) == 0);

    // TEST UPDATE
    Medicine *newMedicine = createMedicine("Algocalmin", 20, 7, 6);
    addToService(service, getName(medicine), getConcentration(medicine), getQuantity(medicine), getPrice(medicine));
    updateInService(service, getName(newMedicine), getConcentration(newMedicine), getQuantity(newMedicine),
                    getPrice(newMedicine));
    assert(*getName(service->repository->medicines->elements[0]) == *getName(newMedicine));
    assert(getConcentration(service->repository->medicines->elements[0]) == getConcentration(newMedicine));
    assert(getQuantity(service->repository->medicines->elements[0]) == getQuantity(newMedicine));
    assert(getPrice(service->repository->medicines->elements[0]) == getPrice(newMedicine));
    destroyMedicine(medicine);
    destroyMedicine(newMedicine);
    destroyService(service);
}

void testAll() {
    testDomain();
    testDynamicArray();
    testRepository();
    testService();
    printf("GG EASY!\n");
}
