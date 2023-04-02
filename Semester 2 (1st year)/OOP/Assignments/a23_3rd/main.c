#include <stdio.h>
#include "medicine.h"
#include "repository.h"
#include "dynamicArray.h"
#include "service.h"
#include "ui.h"
#include "tests.h"
#include <crtdbg.h>


int main()
{
    Repository* repository = createRepository();
    Service* service = createService(repository);
    Console* console = createConsole(service);
    void testCreateRepository();
    void test_createDynamicArray();
    void test_addMedicineRepository();
    void test_deleteRepository();
    void test_updateRepository();
    startMenu(console);
    destroyConsole(console);
    _CrtDumpMemoryLeaks();
    return 0;
}