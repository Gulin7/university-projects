#include "service.h"

Service* createService(Repository* repo, OperationStack* undo, OperationStack* redo)
{
    return NULL;
}

void destroyService(Service* service)
{
}

Repository* getRepository(Service* service)
{
    return NULL;
}

int addService(Service* service, char* name, int concentration, int quantity, double price)
{
    return 0;
}

int deleteService(Service* service, char* name, int concentration)
{
    return 0;
}

int updateService(Service* service, char* name, int concentration, int newQuantity, double newPrice)
{
    return 0;
}

void sortService(Service* service)
{
}

void generateMedicines(Service* service)
{
}

int getServiceSize(Service* service)
{
    return 0;
}

Repository* filterByPrice(Repository* repository, double price)
{
    return NULL;
}

int undo(Service* service)
{
    return 0;
}

int redo(Service* service)
{
    return 0;
}
