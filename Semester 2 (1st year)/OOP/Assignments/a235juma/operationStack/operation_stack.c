//
// Created by gulin on 05/04/2023.
//

#include "operation_stack.h"
#include <string.h>

Operation *createOperation(Medicine *medicine, char *type) {

    Operation *operation = (Operation *) malloc(sizeof(Operation));

    operation->medicine = medicine;
    operation->type = (char *) malloc(sizeof(char) * strlen(type) + 1);

    strcpy(operation->type, type);

    return operation;
}

void destroyOperation(Operation *operation) {
    //destroyMedicine(operation->medicine);
    free(operation->type);
    free(operation);
}

Operation *operationCopy(Operation *operation) {
    Operation *newOperation = createOperation(getOperationMedicine(operation), getOperationType(operation));
    return newOperation;
}

Medicine *getOperationMedicine(Operation *operation) {
    return operation->medicine;
}

char *getOperationType(Operation *operation) {
    return operation->type;
}

OperationStack *createOperationStack() {
    OperationStack *operationStack = (OperationStack *) malloc(sizeof(OperationStack));
    if (operationStack == NULL) {
        return NULL;
    }

    operationStack->operations = createArray(20);

    return operationStack;
}

void destroyOperationStack(OperationStack *stack) {
    destroyArray(stack->operations);
    free(stack);
}

void push(OperationStack *stack, Operation *operation) {
    Operation *newOperation = operationCopy(operation);
    addNewElement(stack->operations, newOperation);
    destroyOperation(newOperation);
}

Operation *pop(OperationStack *stack) {
    if (getSizeArray(stack->operations) == 0)
        return NULL;

    Operation *operation = operationCopy( stack->operations->elements[stack->operations->size - 1]);
    stack->operations->size--;

    return operation;
}