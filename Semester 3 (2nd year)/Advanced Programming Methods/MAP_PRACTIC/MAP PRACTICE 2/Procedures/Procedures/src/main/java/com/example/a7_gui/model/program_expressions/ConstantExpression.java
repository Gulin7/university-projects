package com.example.a7_gui.model.program_expressions;

import com.example.a7_gui.exceptions.*;
import com.example.a7_gui.exceptions.ArithmeticException;
import com.example.a7_gui.model.program_types.IntType;
import com.example.a7_gui.model.program_types.Type;
import com.example.a7_gui.model.my_utils.MyIDictionary;
import com.example.a7_gui.model.my_utils.MyIHeap;
import com.example.a7_gui.model.program_values.IntValue;
import com.example.a7_gui.model.program_values.Value;


public class ConstantExpression implements IExpression{
    private int value;

    public ConstantExpression(Integer value){
        this.value=value;
    }

    @Override
    public Type typeCheck(MyIDictionary<String, Type> typeEnv) throws EvaluationException, DataStructureException {
        return null;
    }

    @Override
    public Value evaluateExpression(MyIDictionary<String, Value> table, MyIHeap heap) throws EvaluationException, DataStructureException, ArithmeticException {
        return null;
    }

    @Override
    public IExpression deepCopy() {
        return null;
    }

    public String toString()
    {
        return String.format("const(%d)", value);
    }
}
