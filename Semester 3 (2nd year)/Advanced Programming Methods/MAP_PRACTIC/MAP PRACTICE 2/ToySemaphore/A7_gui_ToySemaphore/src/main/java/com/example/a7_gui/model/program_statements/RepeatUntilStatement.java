package com.example.a7_gui.model.program_statements;

import com.example.a7_gui.exceptions.ADTException;
import com.example.a7_gui.exceptions.DivisionByZero;
import com.example.a7_gui.exceptions.ExpressionEvaluationException;
import com.example.a7_gui.exceptions.StatementExecutionException;
import com.example.a7_gui.model.my_utils.MyIStack;
import com.example.a7_gui.model.program_expressions.IExpression;
import com.example.a7_gui.model.programState.ProgramState;
import com.example.a7_gui.model.program_expressions.OppositeExpression;
import com.example.a7_gui.model.program_expressions.RelationalExpression;
import com.example.a7_gui.model.program_types.BoolType;
import com.example.a7_gui.model.program_types.IntType;
import com.example.a7_gui.model.program_types.StringType;
import com.example.a7_gui.model.program_types.Type;
import com.example.a7_gui.model.my_utils.MyIDictionary;
import com.example.a7_gui.model.values.IntValue;
import com.example.a7_gui.model.values.StringValue;
import com.example.a7_gui.model.values.Value;

public class RepeatUntilStatement implements IStatement{
    private final IStatement innerStmt;
    private final IExpression condExpr;

    public RepeatUntilStatement(IExpression condExpr, IStatement innerStmt)
    {
        this.condExpr=condExpr;
        this.innerStmt=innerStmt;
    }

    @Override
    public ProgramState execute(ProgramState state) throws StatementExecutionException, ExpressionEvaluationException, ADTException, DivisionByZero {
        MyIStack<IStatement> exeStack = state.getExecutionStack();
        IStatement whileStmt = new CompoundStatement(innerStmt, new WhileStatement(new OppositeExpression(condExpr), innerStmt));

        exeStack.push(whileStmt);
        state.setExeStack(exeStack);

        return null;
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws StatementExecutionException, ExpressionEvaluationException, ADTException {
        Type type = condExpr.typeCheck(typeEnv);
        if(type.equals(new BoolType()))
        {
            innerStmt.typeCheck(typeEnv.deepCopy());
            return typeEnv;
        }
        else throw new StatementExecutionException("Expression from >>repeat until<< must be of type bool");
    }

    @Override
    public IStatement deepCopy() {
        return new RepeatUntilStatement(condExpr.deepCopy(), innerStmt.deepCopy());
    }

    @Override
    public String toString() {
        return String.format("repeat(%s) until (%s)", innerStmt, condExpr);
    }
}
