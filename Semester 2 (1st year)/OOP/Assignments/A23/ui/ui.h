//
// Created by Tudor on 14/03/2023.
//

#ifndef A23_GULIN7_UI_H
#define A23_GULIN7_UI_H

#define _CRT_SECURE_NO_WARNINGS 1

#include "../services/service.h"

/*
 * Struct that stores the UI information.
 * */
typedef struct {
    Service *service;
} UI;

/*
 */
UI *createUI(Service *service);

/*
*/
void destroyUI(UI *ui);

/*
 * Main function
 * */
void runUi(UI *ui);

#endif //A23_GULIN7_UI_H
