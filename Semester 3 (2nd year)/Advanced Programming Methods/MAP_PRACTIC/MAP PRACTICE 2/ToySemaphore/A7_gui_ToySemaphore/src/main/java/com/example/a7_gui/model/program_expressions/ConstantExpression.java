package com.example.a7_gui.model.program_expressions;

import com.example.a7_gui.exceptions.ADTException;
import com.example.a7_gui.exceptions.DivisionByZero;
import com.example.a7_gui.exceptions.ExpressionEvaluationException;
import com.example.a7_gui.model.program_types.BoolType;
import com.example.a7_gui.model.program_types.IntType;
import com.example.a7_gui.model.program_types.Type;
import com.example.a7_gui.model.my_utils.MyIDictionary;
import com.example.a7_gui.model.my_utils.MyIHeap;
import com.example.a7_gui.model.values.BoolValue;
import com.example.a7_gui.model.values.IntValue;
import com.example.a7_gui.model.values.Value;

public class ConstantExpression implements IExpression{
    private int value;

    public ConstantExpression(Integer value){
        this.value=value;
    }

    @Override
    public Type typeCheck(MyIDictionary<String, Type> typeEnv) throws ExpressionEvaluationException, ADTException {
        return null;
    }

    @Override
    public Value evaluateExpression(MyIDictionary<String, Value> table, MyIHeap heap) throws ExpressionEvaluationException, ADTException, DivisionByZero {
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
