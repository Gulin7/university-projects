package com.example.a7_gui.model.program_statements;

import com.example.a7_gui.exceptions.ADTException;
import com.example.a7_gui.exceptions.DivisionByZero;
import com.example.a7_gui.exceptions.ExpressionEvaluationException;
import com.example.a7_gui.exceptions.StatementExecutionException;
import com.example.a7_gui.model.my_utils.MyIStack;
import com.example.a7_gui.model.program_expressions.IExpression;
import com.example.a7_gui.model.programState.ProgramState;
import com.example.a7_gui.model.program_expressions.RelationalExpression;
import com.example.a7_gui.model.program_expressions.ValueExpression;
import com.example.a7_gui.model.program_types.IntType;
import com.example.a7_gui.model.program_types.StringType;
import com.example.a7_gui.model.program_types.Type;
import com.example.a7_gui.model.my_utils.MyIDictionary;
import com.example.a7_gui.model.values.IntValue;
import com.example.a7_gui.model.values.StringValue;
import com.example.a7_gui.model.values.Value;

public class WaitStatement implements IStatement{
    private final int value;

    public WaitStatement(int value)
    {
        this.value=value;
    }
    @Override
    public ProgramState execute(ProgramState state) throws StatementExecutionException, ExpressionEvaluationException, ADTException, DivisionByZero {
        if(value != 0)
        {
            MyIStack<IStatement> exeStack = state.getExecutionStack();
            exeStack.push(new CompoundStatement(new PrintStatement(new ValueExpression(new IntValue(value))), new WaitStatement(value - 1)));
            state.setExeStack(exeStack);
        }

        return null;
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws StatementExecutionException, ExpressionEvaluationException, ADTException {
        return typeEnv;
    }

    @Override
    public IStatement deepCopy() {
        return new WaitStatement(value);
    }

    @Override
    public String toString() {
        return String.format("wait(%s)", value);
    }
}
