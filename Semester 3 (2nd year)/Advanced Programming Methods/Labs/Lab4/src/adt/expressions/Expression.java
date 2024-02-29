package adt.expressions;

import adt.adts.MyIDictionary;
import adt.values.Value;
import controller.ExpressionEvaluationException;

public interface Expression {
    Value evaluate(MyIDictionary<String, Value> table) throws ExpressionEvaluationException;
}
