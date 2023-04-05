#include "Tests.h"
#include <assert.h>
#include <string.h>

void testMedicine()
{
	Medicine medicine = createMedicine("Decasept", 5, 10, 2);
	
	// TEST GETTERS
	assert(getConcentration(medicine) == 5);
	assert(getQuantity(medicine) == 10);
	assert(getPrice(medicine) == 2);

	// TEST SETTERS
	setName(&medicine, "Rares");
	setConcentration(&medicine, 69);
	setQuantity(&medicine, 2);
	setPrice(&medicine, 3);
	assert(strcmp(getName(medicine), "Rares") == 0);
	assert(getConcentration(medicine) == 69);
	assert(getQuantity(medicine) == 2);
	assert(getPrice(medicine) == 3);
}

void testRepo()
{
	Repository* repository = createRepository();
	addMedicine(repository, "Filip", 1, 2, 3);
	addMedicine(repository, "Dania", 5, 6, 7);
    printf("%d", repository->medicines[1]);
	assert(repository->size == 2);
	//
	assert(getConcentration(repository->medicines[0]) == 1);
	assert(getConcentration(repository->medicines[1]) == 5);
	//
	assert(getQuantity(repository->medicines[0]) == 2);	
	assert(getQuantity(repository->medicines[0]) == 6);
	//
	assert(getPrice(repository->medicines[0]) == 3);
	assert(getPrice(repository->medicines[1]) == 7);
	//
	updateMedicine(repository, "Filip", 1, 20, 30);
	assert(getQuantity(repository->medicines[0]) == 20);
	assert(getPrice(repository->medicines[0]) == 30);
	//
	deleteMedicine(repository, "Filip", 1);
	assert(repository->size == 1);
}

void testService()
{
	Repository* repository = createRepository();
	Service* service = createService(repository);
	//
	addMedicineService(service, "Alfred", 2, 5, 10);
	assert(getConcentration(service->repository->medicines[0]) == 2);
	assert(getQuantity(service->repository->medicines[0]) == 5);
	assert(getPrice(service->repository->medicines[0]) == 10);
	//
	updateMedicineService(service, "Alfred", 2, 100, 200);
	assert(getQuantity(service->repository->medicines[0]) == 100);
	assert(getPrice(service->repository->medicines[0]) == 200);
	//
	deleteMedicineService(service, "Alfred", 2);
	assert(getSizeRepository(service->repository) == 0);

}

void allTests()
{
	testMedicine();
	testRepo();
	testService();
}
