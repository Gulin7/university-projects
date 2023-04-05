#pragma once
#include "Service.h"

typedef struct {
	Service* service;
}Ui;

Ui createUi(Service* service);

void runUi(Ui ui);