package domain.statements;

import exceptions.ExpressionException;
import domain.dataTypes.IValue;
import domain.utils.MyIDictionary;
import domain.ProgramState;
import domain.expressions.IExpression;

public class AssignStatement implements IStatement {
    private final String variableId;
    private final IExpression expressionToAssign;

    public AssignStatement(String variableId, IExpression expressionToAssign)
    {
        this.variableId = variableId;
        this.expressionToAssign = expressionToAssign;
    }

    @Override
    public ProgramState execute(ProgramState currentState) throws ExpressionException {
        MyIDictionary<String, IValue> symbolTable = currentState.getSymbolTable();

        if (!symbolTable.exists(variableId))
            throw new ExpressionException("Variable " + variableId + " not defined!");

        IValue valueToAssign = expressionToAssign.evaluateExpression(symbolTable);

        IValue variableValue = symbolTable.getValue(variableId);

        if (!valueToAssign.getType().equals(variableValue.getType()))
            throw new ExpressionException("Different variable types!");

        symbolTable.add(variableId, valueToAssign);

        return currentState;
    }

    @Override
    public String toString() {
        return "(" + variableId + "=" + expressionToAssign + ")";
    }
}

