package domain.statements;

import exceptions.StatementException;
import domain.*;
import domain.dataTypes.*;
import domain.utils.MyIDictionary;

public class VariableDeclarationStatement implements IStatement {
    private final String variableId;
    private final IType variableType;

    public VariableDeclarationStatement(String variableId, IType variableType)
    {
        this.variableId = variableId;
        this.variableType = variableType;
    }

    @Override
    public ProgramState execute(ProgramState currentState) throws StatementException {
        MyIDictionary<String, IValue> symbolTable = currentState.getSymbolTable();

        if (symbolTable.exists(variableId))
            throw new StatementException("Variable already defined!");

        if (variableType.equals(new IntType()))
            symbolTable.add(variableId, new IntValue(0));

        else
            symbolTable.add(variableId, new BoolValue(false));

        return currentState;
    }

    @Override
    public String toString() {
        return "(" + variableType + " " + variableId +  ')';
    }
}
