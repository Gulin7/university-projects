//
// Created by gulin on 05/04/2023.
//

#ifndef A235JUMA_UI_H
#define A235JUMA_UI_H

#define _CRT_SECURE_NO_WARNINGS

#include "../services/service.h"

/*
 * Struct that stores the Ui information.
 * */
typedef struct {
    Service *service;
} Ui;

/*
 */
Ui *createUI(Service *service);

/*
*/
void destroyUI(Ui *ui);

/*
 * Main function
 * */
void runUi(Ui *ui);

#endif //A235JUMA_UI_H
