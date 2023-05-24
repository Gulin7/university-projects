#pragma once
#include "service.h"

typedef struct {
	Service* service;
}Ui;

Ui* createUi(Service *service);

void destroyUi(Ui* ui);

void runUi(Ui* ui);
