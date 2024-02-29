package adt.statements.filesStmts;

import adt.ProgramState;
import adt.adts.MyIDictionary;
import adt.expressions.Expression;
import adt.statements.IStmt;
import adt.types.IntType;
import adt.types.StringType;
import adt.values.IntValue;
import adt.values.StringValue;
import adt.values.Value;
import controller.ExpressionEvaluationException;
import controller.StatementExecutionException;

import javax.swing.plaf.nimbus.State;
import java.io.BufferedReader;
import java.io.IOException;

public class ReadFileStmt implements IStmt {
    Expression expression;
    String varName;
    public ReadFileStmt(Expression expression, String varName)
    {
        this.expression = expression;
        this.varName = varName;
    }
    @Override
    public ProgramState execute(ProgramState state) throws StatementExecutionException, ExpressionEvaluationException, IOException {
        MyIDictionary<String, Value> symbolTable = state.getSymbolTable();
        Value value = symbolTable.lookUp(varName);
        if(value.getType().equals(new IntType()))
        {
            Value fileName = expression.evaluate(symbolTable);
            if(fileName.getType().equals(new StringType()) )
            {
                MyIDictionary<StringValue, BufferedReader>  fileTable = state.getFileTable();
                if(fileTable.isDefined((StringValue)fileName))
                {
                    try
                    {
                        BufferedReader descr =  fileTable.lookUp((StringValue)fileName);
                        String readValue = descr.readLine();
                        int readValInt = 0;
                        if(readValue != null)
                            readValInt = Integer.parseInt(readValue);
                        symbolTable.update(varName, new IntValue(readValInt));
                        return state;
                    }
                    catch (IOException exception){
                        throw new StatementExecutionException("Couldn't read line");
                    }
                }
            }
            else {
                throw new StatementExecutionException("Filename must be string");
            }
        }
        throw new StatementExecutionException("Variable must be of IntType");
    }

    @Override
    public String toString() {
        return "ReadFile(" +
                expression.toString() +
                ", " + varName.toString() +')';
    }
}
