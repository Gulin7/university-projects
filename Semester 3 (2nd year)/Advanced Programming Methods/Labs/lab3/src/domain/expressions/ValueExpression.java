package domain.expressions;

import domain.dataTypes.IValue;
import domain.utils.MyIDictionary;

public class ValueExpression implements IExpression {
    private final IValue value;

    public ValueExpression(IValue value) {
        this.value = value;
    }

    @Override
    public IValue evaluateExpression(MyIDictionary<String, IValue> symbolTable) {
        return this.value;
    }

    @Override
    public String toString() {
        return this.value.toString();
    }
}
