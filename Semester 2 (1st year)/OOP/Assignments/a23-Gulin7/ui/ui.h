//
// Created by Tudor on 14/03/2023.
//

#ifndef A23_GULIN7_UI_H
#define A23_GULIN7_UI_H

#define _CRT_SECURE_NO_WARNINGS 1

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

#endif //A23_GULIN7_UI_H
