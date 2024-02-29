package adt.statements;

import adt.ProgramState;
import adt.adts.MyIDictionary;
import adt.adts.MyIStack;
import adt.expressions.Expression;
import adt.types.BoolType;
import adt.values.BoolValue;
import adt.values.Value;
import controller.ExpressionEvaluationException;
import controller.StatementExecutionException;

public class IfStmt implements IStmt {
    Expression expression;
    IStmt thenStmt;
    IStmt elseStmt;
    public IfStmt(Expression expression, IStmt tStmt, IStmt eStmt)
    {
        this.expression = expression;
        thenStmt = tStmt;
        elseStmt = eStmt;
    }

    @Override
    public String toString(){
        return "if ("+ expression.toString()+") \n{\n " + thenStmt.toString() +"\n}\nelse\n{\n "+ elseStmt.toString()+"\n}";
    }

    public ProgramState execute(ProgramState state) throws StatementExecutionException, ExpressionEvaluationException {
        MyIDictionary<String, Value> symTable = state.getSymbolTable();
        Value expectedBool = expression.evaluate(symTable);
        if(expectedBool.getType().equals(new BoolType()))
        {
            MyIStack<IStmt> stack = state.getExecutionStack();
            BoolValue boolExpressionValue = (BoolValue) expectedBool;
            if((Boolean) boolExpressionValue.getValue())
                stack.push(thenStmt);
            else
                stack.push(elseStmt);
            return state;
        }
        throw new StatementExecutionException("expression is not of boolean type");
    }
}
