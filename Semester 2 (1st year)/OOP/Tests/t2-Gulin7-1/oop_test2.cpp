#include <iostream>
#include <crtdbg.h>
#include "Ui.h"
#include "Controller.h"

int main()
{
    try
    {
        std::cout << "Start app!";
        Controller controller = Controller();
        Ui ui = Ui(controller);
        ui.runUi();
    }
    catch (std::runtime_error) {
        std::cout << "Cannot open given file!";
    }
    return 0;
}
