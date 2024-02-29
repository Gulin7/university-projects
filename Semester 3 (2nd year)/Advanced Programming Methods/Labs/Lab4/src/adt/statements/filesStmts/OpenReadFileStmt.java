package adt.statements.filesStmts;

import adt.ProgramState;
import adt.adts.MyIDictionary;
import adt.expressions.Expression;
import adt.expressions.VariableExpression;
import adt.statements.IStmt;
import adt.types.StringType;
import adt.values.StringValue;
import adt.values.Value;
import controller.ExpressionEvaluationException;
import controller.StatementExecutionException;

import javax.swing.plaf.nimbus.State;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.Reader;


public class OpenReadFileStmt implements IStmt {

    Expression expression;

    public OpenReadFileStmt(Expression expression) {
        this.expression = expression;
    }

    @Override
    public ProgramState execute(ProgramState state) throws StatementExecutionException, ExpressionEvaluationException, IOException {

        Value value = expression.evaluate(state.getSymbolTable());
        if(value.getType().equals(new StringType()))
        {
            MyIDictionary<StringValue, BufferedReader> fileTable =state.getFileTable();
            StringValue filename = (StringValue) value;
            if(fileTable.isDefined(filename))
                throw new StatementExecutionException("File already open");
            else{
                try {
                    Reader reader =  new FileReader(filename.getValue());
                    BufferedReader fileDesc = new BufferedReader(reader);
                    fileTable.put(filename, fileDesc);
                }
                catch(IOException ex){
                    throw new StatementExecutionException("Couldn't open the file");

                }
            }
        }
        else{
            throw new StatementExecutionException("Expression must be String");
        }
        return state;
    }
    @Override
    public String toString()
    {
        return "OpenFile(" + this.expression.toString() + ")";
    }


}