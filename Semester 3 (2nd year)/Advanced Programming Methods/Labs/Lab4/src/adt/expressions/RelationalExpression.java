package adt.expressions;

import adt.adts.MyIDictionary;
import adt.types.IntType;
import adt.values.BoolValue;
import adt.values.IntValue;
import adt.values.Value;
import controller.ExpressionEvaluationException;

public class RelationalExpression implements Expression {

    private Expression expression1;
    private Expression expression2;
    private String compareOperator;

    public RelationalExpression(Expression ex1, Expression ex2, String compareOperator) {
        expression1 = ex1;
        expression2 = ex2;
        this.compareOperator = compareOperator;
    }

    @Override
    public Value evaluate(MyIDictionary<String, Value> symbolTable) throws ExpressionEvaluationException {
        Value value1 = expression1.evaluate(symbolTable);
        Value value2 = expression2.evaluate(symbolTable);
        if (value1.getType().equals(new IntType())) {
            if (value2.getType().equals(new IntType())) {
                IntValue intVal1 = (IntValue) value1;
                int firstValue = (int) intVal1.getValue();

                IntValue intVal2 = (IntValue) value2;
                int secondValue = (int) intVal2.getValue();
                if (compareOperator.equals("<")) {
                    return new BoolValue(firstValue < secondValue);
                } else if (compareOperator.equals("<=")) {
                    return new BoolValue(firstValue <= secondValue);
                } else if (compareOperator.equals("==")) {
                    return new BoolValue(firstValue == secondValue);
                } else if (compareOperator.equals("!=")) {
                    return new BoolValue(firstValue != secondValue);
                } else if (compareOperator.equals(">")) {
                    return new BoolValue(firstValue > secondValue);
                } else if (compareOperator.equals(">=")) {
                    return new BoolValue(firstValue >= secondValue);
                }

                throw new ExpressionEvaluationException("Unsupported operand");

            } else throw new ExpressionEvaluationException("Second expression is not of IntType");
        }
        throw new ExpressionEvaluationException("First expression is not of IntType");
    }

    public String toString() {
        return expression1.toString() + " " + compareOperator + " " + expression2.toString();
    }

}
