#include <iostream>
#include "Tests.h"
#include "Service.h"
#include "Repository.h"
#include "Ui.h"


int main()
{
    Tests test;
    test.testAll();

    std::vector<Car> initialCars = {};
    Repository repository{ initialCars };
    Service service{ repository };
    Ui ui{ service };
    ui.runUi();
}

