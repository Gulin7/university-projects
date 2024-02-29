#include <stdio.h>
#include "Planet.h"
#include "Planet.c"



int main() {

	Planet p = createPlanet("HD 189733 b", "a blue-ish planet", 19);

	_CrtDumpMemoryLeaks();

	return 0;
}