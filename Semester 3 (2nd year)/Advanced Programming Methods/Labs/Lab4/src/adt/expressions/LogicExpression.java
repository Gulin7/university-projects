package adt.expressions;

import adt.adts.MyIDictionary;
import adt.types.BoolType;
import adt.values.BoolValue;
import adt.values.Value;
import controller.ExpressionEvaluationException;

public class LogicExpression implements Expression {
    Expression expression1;

    Expression expression2;
    int operator; //1 - &&, 2 - ||

    public LogicExpression(Expression expression1, Expression expression2, int operator) {
        this.expression1 = expression1;
        this.expression2 = expression2;
        this.operator = operator;
    }

    @Override
    public String toString(){
        if (operator == 1)
        {
            return expression1.toString() + " && " + expression2.toString();
        }
        else
        {
            return expression1.toString() + " || " + expression2.toString();
        }
    }
    @Override
    public Value evaluate(MyIDictionary<String, Value> table) throws ExpressionEvaluationException
    {
        Value value1, value2;
        value1 = expression1.evaluate(table);

        if(value1.getType().equals(new BoolType()))
        {
            value2 = expression2.evaluate(table);
            if(value2.getType().equals(new BoolType()))
            {
                BoolValue bool1 = (BoolValue) value1;
                BoolValue bool2 = (BoolValue) value2;
                boolean number1, number2;
                number1 = (boolean)bool1.getValue();
                number2 = (boolean)bool2.getValue();
                if(operator == 1)
                {
                    return new BoolValue(number1 && number2);
                }
                if(operator == 2)
                {
                    return new BoolValue(number1 || number2);
                }

            }
            else throw new ExpressionEvaluationException("Second operand is not a boolean");
        }
        throw new ExpressionEvaluationException("First operand is not a boolean");
    }
}
