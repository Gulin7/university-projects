#include "repository.h"
#include "dynamicArray.h"
#include "undoRedo.h"
#include "medicine.h"
#include "service.h"
#include "ui.h"

int main() {
    testAll();

    Repository* repository = createRepository();
    OperationStack* undoStack = createOperationStack();
    OperationStack* redoStack = createOperationStack();

    Service* service = createService(repository, undoStack, redoStack);

    Ui* ui = createUI(service);

    runUi(ui);

    destroyUI(ui);
    return 0;
}