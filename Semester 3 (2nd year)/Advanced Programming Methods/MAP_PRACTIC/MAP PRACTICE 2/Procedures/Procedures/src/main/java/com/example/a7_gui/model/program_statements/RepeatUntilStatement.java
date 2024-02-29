package com.example.a7_gui.model.program_statements;

import com.example.a7_gui.exceptions.DataStructureException;
import com.example.a7_gui.exceptions.ArithmeticException;
import com.example.a7_gui.exceptions.EvaluationException;
import com.example.a7_gui.exceptions.ExecutionException;
import com.example.a7_gui.model.program_expressions.IExpression;
import com.example.a7_gui.model.programState.ProgramState;
import com.example.a7_gui.model.program_expressions.OppositeExpression;
import com.example.a7_gui.model.program_expressions.VariableExpression;
import com.example.a7_gui.model.program_types.BoolType;
import com.example.a7_gui.model.program_types.Type;
import com.example.a7_gui.model.my_utils.MyIDictionary;
import com.example.a7_gui.model.my_utils.MyIStack;
import com.example.a7_gui.model.program_values.BoolValue;
import com.example.a7_gui.model.program_values.Value;

public class RepeatUntilStatement implements IStatement{
    private final IStatement innerStmt;
    private final IExpression condExpr;

    public RepeatUntilStatement(IExpression condExpr, IStatement innerStmt)
    {
        this.condExpr=condExpr;
        this.innerStmt=innerStmt;
    }

    @Override
    public ProgramState execute(ProgramState state) throws ExecutionException, EvaluationException, DataStructureException, ArithmeticException{
        MyIStack<IStatement> exeStack = state.getExecutionStack();
        IStatement whileStmt = new CompoundStatement(innerStmt, new WhileStatement(new OppositeExpression(condExpr), innerStmt));

        exeStack.push(whileStmt);
        state.setExeStack(exeStack);

        return null;
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws ExecutionException, EvaluationException, DataStructureException {
        Type type = condExpr.typeCheck(typeEnv);
        if(type.equals(new BoolType()))
        {
            innerStmt.typeCheck(typeEnv.deepCopy());
            return typeEnv;
        }
        else throw new ExecutionException("Expression from >>repeat until<< must be of type bool");
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
