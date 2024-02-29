package source.domain.expressions;

import source.domain.adts.MyIDictionary;
import source.domain.adts.MyIHeap;
import source.domain.types.Type;
import source.exceptions.InterpreterException;
import source.domain.values.IValue;

public class ValueExpression implements IExpression {
    private final IValue value;

    public ValueExpression(IValue value)
    {
        this.value = value;
    }

    @Override
    public IValue evaluate(MyIDictionary<String, IValue> symbolTable, MyIHeap heapTable, int threadID) {
        return value;
    }

    @Override
    public Type typeCheck(MyIDictionary<String, Type> typeTable) throws InterpreterException {
        return value.getType();
    }

    @Override
    public String toString() {
        return value.toString();
    }
}
