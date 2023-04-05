//
// Created by gulin on 05/04/2023.
//

#include "Tests.h"
#include "Ui.h"
#include <crtdbg.h>

int main() {
    allTests();

    Repository* repository = createRepository();
    Service* service = createService(repository);
    Ui ui = createUi(service);
    runUi(ui);

    _CrtDumpMemoryLeaks();

    return 0;
}