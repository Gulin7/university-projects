package domain.expressions;

import exceptions.ExpressionException;
import domain.dataTypes.BoolValue;
import domain.dataTypes.IValue;
import domain.dataTypes.IntType;
import domain.dataTypes.IntValue;
import domain.utils.MyIDictionary;

public class RelationalExpression implements IExpression {
    private final IExpression firstExpression, secondExpression;
    private final String operation;

    public RelationalExpression(IExpression firstExpression, IExpression secondExpression, String operation) {
        this.firstExpression = firstExpression;
        this.secondExpression = secondExpression;
        this.operation = operation;
    }

    @Override
    public IValue evaluateExpression(MyIDictionary<String, IValue> symbolTable) throws ExpressionException {
        IValue firstValue = this.firstExpression.evaluateExpression(symbolTable);
        IValue secondValue = this.secondExpression.evaluateExpression(symbolTable);

        if (!firstValue.getType().equals(new IntType()))
            throw new ExpressionException("First operand does not evaluate to an IntType!");

        if (!secondValue.getType().equals(new IntType()))
            throw new ExpressionException("Second operand does not evaluate to an IntType!");

        int firstInteger = ((IntValue) firstValue).getValue();
        int secondInteger = ((IntValue) secondValue).getValue();

        return switch (operation) {
            case "<" -> new BoolValue(firstInteger < secondInteger);
            case "<=" -> new BoolValue(firstInteger <= secondInteger);
            case "==" -> new BoolValue(firstInteger == secondInteger);
            case "!=" -> new BoolValue(firstInteger != secondInteger);
            case ">" -> new BoolValue(firstInteger > secondInteger);
            case ">=" -> new BoolValue(firstInteger >= secondInteger);
            default -> throw new ExpressionException("Invalid comparison between operands!");
        };

    }

    @Override
    public String toString() {
        return super.toString();
    }

}
