//
// Created by gulin on 29/03/2023.
//

#ifndef A23_VOI_TRECE_PRIN_MONITOR_UI_H
#define A23_VOI_TRECE_PRIN_MONITOR_UI_H

#include "../service/service.h"

/*
 *
 */
typedef struct {
    Service *service;
} Ui;

/*
 *
 */
Ui *createUi(Service *service);;

/*
 *
 */
void destroyUi(Ui *ui);

/*
 *
 */
void runUi(Ui *ui);

#endif //A23_VOI_TRECE_PRIN_MONITOR_UI_H
