package adt.expressions;

import adt.adts.MyIDictionary;
import adt.values.Value;
import controller.ExpressionEvaluationException;

public class VariableExpression implements Expression {
    String variable;

    public VariableExpression(String variable) {
        this.variable = variable;
    }

    @Override
    public String toString(){
        return variable;
    }

    @Override
    public Value evaluate(MyIDictionary<String, Value> table) throws ExpressionEvaluationException {
        if (table.isDefined(variable))
        {
            return table.lookUp(variable);
        }

        throw new ExpressionEvaluationException("variable \"" + variable + "\" not defined");
    }
}
