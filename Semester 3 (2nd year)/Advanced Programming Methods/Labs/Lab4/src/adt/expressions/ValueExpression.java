package adt.expressions;

import adt.adts.MyIDictionary;
import adt.values.Value;

public class ValueExpression implements Expression {
    Value expression;

    public ValueExpression(Value expression) {
        this.expression = expression;
    }

    @Override
    public String toString(){
        return expression.toString();
    }

    @Override
    public Value evaluate(MyIDictionary<String, Value> table) {
        return expression;
    }
}
