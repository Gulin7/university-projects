//
// Created by Tudor on 24/03/2023.
//

#ifndef A23_OPERATION_STACK_H
#define A23_OPERATION_STACK_H

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


#endif //A23_OPERATION_STACK_H
