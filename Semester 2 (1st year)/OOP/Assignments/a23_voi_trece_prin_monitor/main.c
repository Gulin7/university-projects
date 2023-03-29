#include "test/test.h"
#include "repository/repository.h"
#include "service/service.h"
#include "ui/ui.h"

int main() {
    testAll();

    MedicineRepository *repository = createRepository();
    OperationStack *undoStack = createOperationStack();
    OperationStack *redoStack = createOperationStack();

    Service *service = createService(repository, undoStack, redoStack);
    Ui *ui = createUi(service);
    runUi(ui);

    destroyUi(ui);
    return 0;
}
