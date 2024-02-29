package domain.statements;

import exceptions.ExpressionException;
import exceptions.InterpreterException;
import exceptions.StatementException;
import domain.ProgramState;
import domain.expressions.IExpression;
import domain.dataTypes.*;
import domain.utils.MyIDictionary;

import java.io.BufferedReader;
import java.io.IOException;

public class ReadFileStatement implements IStatement {
    private final IExpression fileNameExpression;
    private final String variableId;

    public ReadFileStatement(IExpression fileNameExpression, String variableId)
    {
        this.fileNameExpression = fileNameExpression;
        this.variableId = variableId;
    }

    @Override
    public ProgramState execute(ProgramState currentState) throws StatementException, ExpressionException, InterpreterException {
        MyIDictionary<String, IValue> symbolTable = currentState.getSymbolTable();
        MyIDictionary<String, BufferedReader> fileTable = currentState.getFileTable();

        if (!symbolTable.isDefined(variableId))
            throw new ExpressionException(String.format("Variable %s is not defined!", variableId));

        IValue variableValue = symbolTable.getValue(variableId);

        if (!variableValue.getType().equals(new IntType()))
            throw new InterpreterException(String.format("Variable %s does not evaluate to IntType", variableId));

        IValue fileNameValue = fileNameExpression.evaluateExpression(symbolTable);

        if (!fileNameValue.getType().equals(new StringType()))
            throw new InterpreterException(String.format("File %s is not opened!", fileNameValue));

        StringValue fileName = (StringValue) fileNameValue;
        BufferedReader openedFile = fileTable.getValue(fileName.getValue());

        try {
            String newValue = openedFile.readLine().strip();
            int valueToAssign;

            if (newValue.isEmpty())
            {
                valueToAssign = 0;
            }
            else {
                valueToAssign = Integer.parseInt(newValue);
            }

            symbolTable.add(variableId, new IntValue(valueToAssign));
        }

        catch (IOException e)
        {
            throw new InterpreterException("Failed to read from file " + fileName.getValue());
        }

        return currentState;
    }

    @Override
    public String toString() {
        return String.format("ReadFile(%s, %s)", this.fileNameExpression, this.variableId);
    }
}
