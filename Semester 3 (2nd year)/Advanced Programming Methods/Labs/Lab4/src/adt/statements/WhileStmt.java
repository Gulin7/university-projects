package adt.statements;

import adt.ProgramState;
import adt.adts.MyIStack;
import adt.expressions.Expression;
import adt.types.BoolType;
import adt.values.Value;
import controller.ExpressionEvaluationException;
import controller.StatementExecutionException;

public class WhileStmt implements IStmt{
    Expression expression;
    IStmt statement;

    public WhileStmt(Expression expression, IStmt statement)
    {
        this.expression = expression;
        this.statement = statement;
    }

    @Override
    public ProgramState execute(ProgramState state) throws StatementExecutionException, ExpressionEvaluationException
    {
        MyIStack<IStmt> stack = state.getExecutionStack();
        stack.pop();
        Value value = expression.evaluate(state.getSymbolTable());
        if(!value.getType().equals(new BoolType())){
            throw new ExpressionEvaluationException("Conditional expression is not a boolean");
        }
        if(value.getValue().equals(true)){
            stack.push(this);
            stack.push(statement);
        }
        return state;
    }
}
