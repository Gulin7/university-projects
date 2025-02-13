#include "Planet.h"
#include <stdlib.h>

Planet createPlanet(char* name, char* type, double dist) {
	Planet p;
	p.name = malloc((strlen(name) + 1)*sizeof(char));
	if (p.name == NULL) {
		return p;
	}
	strcpy(p.name, name);

	p.type = malloc((strlen(type) + 1) * sizeof(char));
	if (p.type == NULL) {
		free(p.name);
		return p;
	}
	strcpy(p.type, type);

	p.distanceFromEarth = dist;
}
void destroyPlanet(Planet p) {
	free(p.name);
	free(p.type);
}

char* getName(Planet);