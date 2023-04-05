//
// Created by gulin on 05/04/2023.
//

#ifndef A235JUMA_OPERATION_STACK_H
#define A235JUMA_OPERATION_STACK_H

#include "../dynamicArray/dynamicArray.h"
#include "../domain/domain.h"


typedef struct {
    Medicine *medicine;
    char *type;
} Operation;

typedef struct {
    DynamicArray *operations;
} OperationStack;

/*
*/
Operation *createOperation(Medicine *medicine, char *type);

/*
 */
void destroyOperation(Operation *operation);

/*
*/
Operation *operationCopy(Operation *operation);

/*
*/
Medicine *getOperationMedicine(Operation *operation);

/*
*/
char *getOperationType(Operation *operation);

/*
*/
OperationStack *createOperationStack();

/*
 */
void destroyOperationStack(OperationStack *stack);

/*
 */
void push(OperationStack *stack, Operation *operation);

/*
*/
Operation *pop(OperationStack *stack);
#endif //A235JUMA_OPERATION_STACK_H
