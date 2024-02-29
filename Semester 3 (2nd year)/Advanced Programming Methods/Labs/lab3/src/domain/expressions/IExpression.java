package domain.expressions;

import domain.utils.MyIDictionary;
import domain.dataTypes.IValue;
import exceptions.ExpressionException;

public interface IExpression {
    IValue evaluateExpression(MyIDictionary<String, IValue> symbolTable) throws ExpressionException;
}
