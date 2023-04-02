#include "test.h"
#include "service.h"
#include <assert.h>
#include <stdlib.h>

void testDomain() {
	char* name = "Paracetamol";
	int concentration = 5, quantity = 3;
	double price = 2;
	Medicine* medicine = createMedicine(name, concentration, quantity, price);
	
	assert(medicine != NULL);
	assert(*getName(medicine) == *name);
	assert(getConcentration(medicine) == concentration);
	assert(getQuantity(medicine) == quantity);
	assert(getPrice(medicine) == price);

	destroyMedicine(medicine);

}

void testDynamicArray() {
	DynamicArray* array = createDynamicArray(10);
	assert(array != NULL);
	assert(array->capacity == 10);
	assert(array->size == 0);

	doubleCapacity(array);

	assert(array->capacity == 20);

	destroyDynamicArray(array);

}

void testRepository() {

	Repository* repo = createRepository();

	assert(repo != NULL);

	char* name = "Paracetamol";
	int concentration = 5, quantity = 3;
	double price = 2;
	Medicine* medicine = createMedicine(name, concentration, quantity, price);
	Medicine* newMedicine = createMedicine(name, concentration, 4, 6);

	addRepository(repo, medicine);
	assert(repo->medicines->elements[getSize(repo) - 1] == medicine);

	assert(find((repo->medicines), medicine) == 0);

	deleteRepository(repo, *getName(medicine), getConcentration(medicine));
	assert(getSize(repo) == 0);
	
	*updateRepository(repo, newMedicine);
	assert(repo->medicines->elements[getSize(repo) - 1] == newMedicine);

	destroyMedicine(medicine);
	destroyMedicine(newMedicine);
	destroyRepository(repo);

}

void testService() {
	Repository* repository = createRepository();
	OperationStack* undoStack = createOperationStack();
	OperationStack* redoStack = createOperationStack();
	Service* service = createService(repository, undoStack, redoStack);
	assert(service != NULL);
	// TESTING ADD
	Medicine* medicine = createMedicine("Algocalmin", 20, 3, 5);
	addToService(service, getName(medicine), getConcentration(medicine), getQuantity(medicine), getPrice(medicine));
	assert(getServiceSize(service) == 1);
	assert(*getName(service->repo->medicines->elements[0]) == *getName(medicine));
	assert(getConcentration(service->repo->medicines->elements[0]) == getConcentration(medicine));
	assert(getQuantity(service->repo->medicines->elements[0]) == getQuantity(medicine));
	assert(getPrice(service->repo->medicines->elements[0]) == getPrice(medicine));

	// TEST DELETE
	deleteFromService(service, getName(medicine), getConcentration(medicine));
	assert(getServiceSize(service) == 0);

	// TEST UPDATE
	Medicine* newMedicine = createMedicine("Algocalmin", 20, 7, 6);
	addToService(service, getName(medicine), getConcentration(medicine), getQuantity(medicine), getPrice(medicine));
	updateInService(service, getName(newMedicine), getConcentration(newMedicine), getQuantity(newMedicine),
		getPrice(newMedicine));
	assert(*getName(service->repo->medicines->elements[0]) == *getName(newMedicine));
	assert(getConcentration(service->repo->medicines->elements[0]) == getConcentration(newMedicine));
	assert(getQuantity(service->repo->medicines->elements[0]) == getQuantity(newMedicine));
	assert(getPrice(service->repo->medicines->elements[0]) == getPrice(newMedicine));

	destroyMedicine(medicine);
	destroyMedicine(newMedicine);
	destroyService(service);

}

void testAll(){
	testDomain();
	testDynamicArray();
	testRepository();
	testService();
	printf("Tests passed!");
}
