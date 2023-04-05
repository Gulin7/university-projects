#include "Tests.h"
#include "Ui.h"
#include <crtdbg.h>

int main() {
	allTests(0);

	Repository* repository = createRepository();
	Service* service = createService(repository);
	Ui ui = createUi(service);
	runUi(ui);

	_CrtDumpMemoryLeaks();

	return 0;
}