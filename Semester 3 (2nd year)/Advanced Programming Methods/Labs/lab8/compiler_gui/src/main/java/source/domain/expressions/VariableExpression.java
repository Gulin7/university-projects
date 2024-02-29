package source.domain.expressions;

import source.domain.adts.MyIDictionary;
import source.domain.adts.MyIHeap;
import source.domain.types.Type;
import source.exceptions.InterpreterException;
import source.domain.values.IValue;

public class VariableExpression implements IExpression {
    private final String id;

    public VariableExpression(String id)
    {
        this.id = id;
    }

    @Override
    public IValue evaluate(MyIDictionary<String, IValue> symbolTable, MyIHeap heapTable, int threadID) {
        return symbolTable.get(id);
    }

    @Override
    public Type typeCheck(MyIDictionary<String, Type> typeTable) throws InterpreterException {
        if (!typeTable.isDefined(id))
            throw new InterpreterException(String.format("Variable %s is not defined!", id));

        return typeTable.get(id);
    }

    @Override
    public String toString() {
        return id;
    }
}
