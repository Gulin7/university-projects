package domain.expressions;

import exceptions.ExpressionException;
import domain.dataTypes.IValue;
import domain.utils.MyIDictionary;

public class VariableExpression implements IExpression {
    private final String id;

    public VariableExpression(String id)
    {
        this.id = id;
    }

    @Override
    public IValue evaluateExpression(MyIDictionary<String, IValue> symbolTable) throws ExpressionException {
        return symbolTable.getValue(this.id);
    }

    @Override
    public String toString() {
        return "(" + this.id + ")";
    }
}