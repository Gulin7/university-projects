//
// Created by Tudor on 14/03/2023.
//

#include "repository/repository.h"

#include "services/service.h"
#include "tests/tests.h"
#include "ui/ui.h"

int main() {
    testAll();

    MedicineRepository *repository = createRepository();
    OperationStack *undoStack = createOperationStack();
    OperationStack *redoStack = createOperationStack();

    Service *service = createService(repository, undoStack, redoStack);

    Ui *ui = createUI(service);

    runUi(ui);

    destroyUI(ui);
    return 0;
}