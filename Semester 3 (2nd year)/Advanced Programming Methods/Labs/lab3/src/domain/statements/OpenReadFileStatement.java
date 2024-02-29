package domain.statements;

import exceptions.ExpressionException;
import exceptions.InterpreterException;
import domain.ProgramState;
import domain.expressions.IExpression;
import domain.dataTypes.IValue;
import domain.dataTypes.StringType;
import domain.dataTypes.StringValue;
import domain.utils.MyIDictionary;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class OpenReadFileStatement implements IStatement {
    private final IExpression fileNameExpression;

    public OpenReadFileStatement(IExpression fileNameExpression)
    {
        this.fileNameExpression = fileNameExpression;
    }

    @Override
    public ProgramState execute(ProgramState currentState) throws ExpressionException, InterpreterException {
        MyIDictionary<String, IValue> symbolTable = currentState.getSymbolTable();
        MyIDictionary<String, BufferedReader> fileTable = currentState.getFileTable();

        IValue fileNameValue = fileNameExpression.evaluateExpression(symbolTable);

        if (!fileNameValue.getType().equals(new StringType()))
            throw new ExpressionException(fileNameExpression + " does not evaluate to a StringValue");

        StringValue fileName = (StringValue) fileNameValue;

        if (fileTable.isDefined(fileName.getValue()))
            throw new InterpreterException(fileName.getValue() + " is already opened!");

        try {
            BufferedReader openedFile = new BufferedReader(new FileReader(fileName.getValue()));
            fileTable.add(fileName.getValue(), openedFile);
        }

        catch (IOException e)
        {
            throw new InterpreterException("Failed to open file " + fileName.getValue());
        }

        return currentState;
    }

    @Override
    public String toString() {
        return "OpenReadFile(" + fileNameExpression + ")";
    }
}
