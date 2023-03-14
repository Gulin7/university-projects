//
// Created by Tudor on 14/03/2023.
//

#include "repository/repository.h"

#include "services/service.h"

#include "ui/ui.h"

int main() {

    MedicineRepository *repository = createRepository();

    Service *service = createService(repository);

    UI *ui = createUI(service);

    runUi(ui);

    destroyUI(ui);
    return 0;
}