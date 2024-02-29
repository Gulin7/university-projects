package com.example.a7_gui.model.program_statements;

import com.example.a7_gui.exceptions.*;
import com.example.a7_gui.exceptions.ArithmeticException;
import com.example.a7_gui.model.program_expressions.IExpression;
import com.example.a7_gui.model.programState.ProgramState;
import com.example.a7_gui.model.program_expressions.VariableExpression;
import com.example.a7_gui.model.program_types.BoolType;
import com.example.a7_gui.model.program_types.Type;
import com.example.a7_gui.model.my_utils.MyIDictionary;
import com.example.a7_gui.model.my_utils.MyIStack;
import com.example.a7_gui.model.program_values.BoolValue;
import com.example.a7_gui.model.program_values.Value;

public class SleepStatement implements IStatement{
    private final int value;

    public SleepStatement(int value)
    {
        this.value=value;
    }
    @Override
    public ProgramState execute(ProgramState state) throws ExecutionException, EvaluationException, DataStructureException, ArithmeticException {
        if(value != 0)
        {
            MyIStack<IStatement> exeStack = state.getExecutionStack();
            //TimeUnit.SECONDS.sleep(1);
            exeStack.push(new SleepStatement(value - 1));
            state.setExeStack(exeStack);
        }

        return null;
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws ExecutionException, EvaluationException, DataStructureException {
        return typeEnv;
    }

    @Override
    public IStatement deepCopy() {
        return new SleepStatement(value);
    }

    @Override
    public String toString() {
        return String.format("sleep(%s)", value);
    }
}
