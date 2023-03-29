//
// Created by gulin on 29/03/2023.
//

#include "undo_redo.h"
#include <string.h>

Operation *createOperation(Medicine *medicine, char *type) {
    Operation *operation = (Operation *) malloc(sizeof(Operation));

    operation->medicine = medicine;
    operation->operationType = (char *) malloc(sizeof(char) * strlen(type) + 1);

    strcpy(operation->operationType, type);

    return operation;
}

void destroyOperation(Operation *operation) {
    destroyMedicine(operation->medicine);
    free(operation->operationType);
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
    return operation->operationType;
}

OperationStack *createOperationStack() {
    OperationStack *operationStack = (OperationStack *) malloc(sizeof(OperationStack));
    // Handling NULL/dangling pointers
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

void pushOperation(OperationStack *stack, Operation *operation) {
    Operation *newOperation = operationCopy(operation);
    addElement(stack->operations, newOperation);
    destroyOperation(newOperation);
}

Operation *popOperation(OperationStack *stack) {
    if (getSizeArray(stack->operations) == 0)
        return NULL;

    Operation *operation = stack->operations->elements[stack->operations->size - 1];
    stack->operations->size--;

    return operation;
}
