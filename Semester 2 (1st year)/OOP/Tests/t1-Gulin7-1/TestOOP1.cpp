#include <iostream>
#include "Ui.h"
#include "Tests.h"
#include "Service.h"
#include "Repository.h"
#include "Player.h"

int main()
{
    /*
    * TESTS
    */
    Tests testing;
    testing.testAll();
    /*
    * RUNNING PROGRAM
    */
    std::vector<Player> initialPlayers = {};
    Repository repository{ initialPlayers };
    Service service{ repository };
    service.generatePlayers();
    Ui ui{ service };
    ui.runUi();

    return 0;
}
