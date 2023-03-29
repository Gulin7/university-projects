//
// Created by gulin on 29/03/2023.
//

#ifndef A23_VOI_TRECE_PRIN_MONITOR_UNDO_REDO_H
#define A23_VOI_TRECE_PRIN_MONITOR_UNDO_REDO_H

#include "../dynamic_array/dynamic_array.h"

typedef struct {
    Medicine *medicine;
    char *operationType;
} Operation;

typedef struct {
    DynamicArray *operations;
} OperationStack;

/*
 *
 */
Operation *createOperation(Medicine *medicine, char *type);

/*
 *
 */
void destroyOperation(Operation *operation);

/*
 *
 */
Operation *operationCopy(Operation *operation);

/*
 *
 */
Medicine *getOperationMedicine(Operation *operation);

/*
 *
 */
char *getOperationType(Operation *operation);

/*
 *
 */
OperationStack *createOperationStack();

/*
 *
 */
void destroyOperationStack(OperationStack *stack);

/*
 *
 */
void pushOperation(OperationStack *stack, Operation *operation);

/*
 *
 */
Operation *popOperation(OperationStack *stack)


#endif //A23_VOI_TRECE_PRIN_MONITOR_UNDO_REDO_H
