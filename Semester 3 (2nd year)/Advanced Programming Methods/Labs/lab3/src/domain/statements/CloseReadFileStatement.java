package domain.statements;

import exceptions.ExpressionException;
import exceptions.InterpreterException;
import exceptions.StatementException;
import domain.ProgramState;
import domain.expressions.IExpression;
import domain.dataTypes.IValue;
import domain.dataTypes.StringType;
import domain.dataTypes.StringValue;
import domain.utils.MyIDictionary;

import java.io.BufferedReader;
import java.io.IOException;


public class CloseReadFileStatement implements IStatement {
    private final IExpression fileNameExpression;

    public CloseReadFileStatement(IExpression fileNameExpression)
    {
        this.fileNameExpression = fileNameExpression;
    }

    @Override
    public ProgramState execute(ProgramState currentState) throws StatementException, ExpressionException, InterpreterException {
        MyIDictionary<String, IValue> symbolTable = currentState.getSymbolTable();
        MyIDictionary<String, BufferedReader> fileTable = currentState.getFileTable();

        IValue fileNameValue = fileNameExpression.evaluateExpression(symbolTable);

        if (!fileNameValue.getType().equals(new StringType()))
            throw new ExpressionException(fileNameExpression + " does not evaluate to a StringType!");

        StringValue fileName = (StringValue) fileNameValue;

        if (!fileTable.isDefined(fileName.getValue()))
            throw new InterpreterException(String.format("File %s is not opened!", fileName));

        BufferedReader fileToClose = fileTable.getValue(fileName.getValue());

        try {
            fileToClose.close();

        }

        catch (IOException e)
        {
            throw new InterpreterException(String.format("Failed to close file %s!", fileName.getValue()));
        }
        return null;
    }

    @Override
    public String toString() {
        return String.format("CloseFile(%s)", this.fileNameExpression);
    }
}
