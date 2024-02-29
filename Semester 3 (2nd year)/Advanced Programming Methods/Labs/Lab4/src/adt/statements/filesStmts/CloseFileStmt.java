package adt.statements.filesStmts;
import adt.ProgramState;
import adt.adts.MyIDictionary;
import adt.expressions.Expression;
import adt.statements.IStmt;
import adt.types.StringType;
import adt.values.StringValue;
import adt.values.Value;
import controller.ExpressionEvaluationException;
import controller.StatementExecutionException;

import java.io.BufferedReader;
import java.io.IOException;

public class CloseFileStmt implements IStmt {
    private Expression expression;

    public CloseFileStmt(Expression expression) {
        this.expression = expression;
    }

    @Override
    public ProgramState execute(ProgramState state) throws StatementExecutionException, ExpressionEvaluationException {
        Value value = expression.evaluate(state.getSymbolTable());
        if(value.getType().equals(new StringType()))
        {
            MyIDictionary<StringValue, BufferedReader> fileTable = state.getFileTable();
            if(fileTable.isDefined((StringValue)value))
            {
                BufferedReader fileDescr = fileTable.lookUp((StringValue)value);
                try {
                    fileTable.remove((StringValue)value);
                    fileDescr.close();
                    return state;
                }
                catch(IOException exception) {
                    throw new StatementExecutionException("Couldn't close file");
                }
            }
            else
                throw new StatementExecutionException("File not found");

        }
        else
            throw new StatementExecutionException("Filename must be StringValue");

    }

    @Override
    public String toString() {
        return "CloseFile(" +
                expression.toString() +
                ')';
    }
}