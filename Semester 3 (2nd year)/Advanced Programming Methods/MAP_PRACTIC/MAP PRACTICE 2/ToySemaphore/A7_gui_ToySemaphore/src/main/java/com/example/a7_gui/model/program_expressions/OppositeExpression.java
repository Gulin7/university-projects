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

public class OppositeExpression implements IExpression{
    private final IExpression innerExpr;

    public OppositeExpression(IExpression innerExpr)
    {
        this.innerExpr=innerExpr;
    }

    @Override
    public Type typeCheck(MyIDictionary<String, Type> typeEnv) throws ExpressionEvaluationException, ADTException {
        return innerExpr.typeCheck(typeEnv);
    }

    @Override
    public Value evaluateExpression(MyIDictionary<String, Value> table, MyIHeap heap) throws ExpressionEvaluationException, ADTException, DivisionByZero {
        BoolValue value = (BoolValue) innerExpr.evaluateExpression(table, heap);

        if(!value.getValue())
            return new BoolValue(true);
        else return new BoolValue(false);
    }

    @Override
    public IExpression deepCopy() {
        return new OppositeExpression(innerExpr.deepCopy());
    }

    @Override
    public String toString() {
        return String.format("!( %s )", innerExpr);
    }
}
