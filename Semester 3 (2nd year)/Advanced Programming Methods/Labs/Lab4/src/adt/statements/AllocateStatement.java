package adt.statements;

import controller.ExpressionEvaluationException;
import adt.ProgramState;
import adt.expressions.Expression;
import adt.values.Value;
import adt.types.ReferenceType;
import adt.values.ReferenceValue;
import adt.adts.MyIDictionary;
import adt.adts.MyIHeap;

public class AllocateStatement implements IStmt {
    // USAGE: new(variable, value) translates into -> new AllocateStatement(variable, value);
    private final String variableName;
    private final Expression expressionToEvaluate;

    public AllocateStatement(String variableName, Expression expression)
    {
        this.variableName = variableName;
        this.expressionToEvaluate = expression;
    }


    @Override
    public ProgramState execute(ProgramState currentState) throws ExpressionEvaluationException {
        MyIDictionary<String, Value> symbolTable = currentState.getSymbolTable();
        MyIHeap heapTable = currentState.getHeapTable();

        // if the variable we want to allocate is not defined stop
        if (!symbolTable.isDefined(variableName))
            throw new ExpressionEvaluationException("Variable: " + variableName + " is not defined in symbol table!");

        // if the variable we want to allocate is not of reference type we stop
        if (!(symbolTable.lookUp(variableName).getType() instanceof ReferenceType))
            throw new ExpressionEvaluationException("Variable: " + variableName + " is not of reference type!");

        // get the variable from symbol table and evaluate the expression
        ReferenceValue variableToAllocate = (ReferenceValue) symbolTable.lookUp(variableName);
        Value expressionValue = expressionToEvaluate.evaluate(symbolTable);

        // get the ReferenceType of the variable from symbol table for further accessing the inner type
        ReferenceType variableType = (ReferenceType) variableToAllocate.getType();

        // check if the inner type is same as expression type
        if (!expressionValue.getType().equals(variableType.getInnerType()))
            throw new ExpressionEvaluationException("Expression does not match location type!");

        // allocate and update the address of the reference
        int addressOfVariable = heapTable.allocate(expressionValue);
        // variableToAllocate.setHeapAddress(addressOfVariable);

        symbolTable.update(variableName, new ReferenceValue(addressOfVariable, variableType.getInnerType()));

        return null;
    }

    @Override
    public String toString() {
        return "new(" + variableName + ", " + expressionToEvaluate.toString() + ")";
    }
}