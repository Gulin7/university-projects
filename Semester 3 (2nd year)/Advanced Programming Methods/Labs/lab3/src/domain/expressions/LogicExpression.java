package domain.expressions;

import exceptions.ExpressionException;
import domain.dataTypes.BoolType;
import domain.dataTypes.BoolValue;
import domain.dataTypes.IValue;
import domain.utils.MyIDictionary;

public class LogicExpression implements IExpression{
    private final IExpression firstExpression, secondExpression;
    private final int operation;

    public LogicExpression(IExpression firstExpression, IExpression secondExpression, int operation)
    {
        this.firstExpression = firstExpression;
        this.secondExpression = secondExpression;
        this.operation = operation;
    }

    @Override
    public IValue evaluateExpression(MyIDictionary<String, IValue> symbolTable) throws ExpressionException {
        IValue firstValue = this.firstExpression.evaluateExpression(symbolTable);
        IValue secondValue = this.secondExpression.evaluateExpression(symbolTable);

        if (!firstValue.getType().equals(new BoolType()))
            throw new ExpressionException("1st op is not bool!");

        if (!secondValue.getType().equals(new BoolType()))
            throw new ExpressionException("2nd op is not bool!");

        BoolValue firstOperand = (BoolValue) firstValue;
        BoolValue secondOperand = (BoolValue) secondValue;

        switch (this.operation)
        {
            case 1: // and
                return new BoolValue(firstOperand.getValue() && secondOperand.getValue());

            case 2: // or
                return new BoolValue(firstOperand.getValue() || secondOperand.getValue());
        }

        throw new ExpressionException("wrong operation");
    }

    @Override
    public String toString() {
        return switch (operation) {
            case 1 -> "(" + firstExpression + " && " + secondExpression + ")";
            case 2 -> "(" + firstExpression + " || " + secondExpression + ")";

            default -> "";
        };
    }
}
