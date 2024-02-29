package domain.expressions;

import exceptions.ExpressionException;
import domain.dataTypes.IValue;
import domain.dataTypes.IntType;
import domain.dataTypes.IntValue;
import domain.utils.MyIDictionary;

public class ArithmeticExpression implements IExpression {
    private final IExpression firstExpression, secondExpression;
    private final char operation;

    public ArithmeticExpression(char operation, IExpression firstExpression, IExpression secondExpression)
    {
        this.firstExpression = firstExpression;
        this.secondExpression = secondExpression;
        this.operation = operation;
    }

    @Override
    public IValue evaluateExpression(MyIDictionary<String, IValue> symbolTable) throws ExpressionException {
        IValue firstValue, secondValue;
        firstValue = this.firstExpression.evaluateExpression(symbolTable);
        secondValue = this.secondExpression.evaluateExpression(symbolTable);

        if (!firstValue.getType().equals(new IntType()))
            throw new ExpressionException("1st op is not int");

        if (!secondValue.getType().equals(new IntType()))
            throw new ExpressionException("2nd op is not int");

        IntValue firstOperand = (IntValue) firstValue;
        int firstNumber = firstOperand.getValue();

        IntValue secondOperand = (IntValue) secondValue;
        int secondNumber = secondOperand.getValue();

        switch (this.operation)
        {
            case '+':
                return new IntValue(firstNumber + secondNumber);

            case '-':
                return new IntValue(firstNumber - secondNumber);

            case '*':
                return new IntValue(firstNumber * secondNumber);

            case '/':
                if (secondNumber == 0)
                    throw new ExpressionException("division by 0! :p");

                return new IntValue(firstNumber / secondNumber);
        }

        return null;
    }

    @Override
    public String toString() {

        return switch (this.operation) {
            case '+' -> "( " + this.firstExpression.toString() + " + " + this.secondExpression.toString() + " )";
            case '-' -> "( " + this.firstExpression.toString() + " - " + this.secondExpression.toString() + " )";
            case '*' -> "( " + this.firstExpression.toString() + " * " + this.secondExpression.toString() + " )";
            case '/' -> "( " + this.firstExpression.toString() + " / " + this.secondExpression.toString() + " )";
            default -> "";
        };
    }
}