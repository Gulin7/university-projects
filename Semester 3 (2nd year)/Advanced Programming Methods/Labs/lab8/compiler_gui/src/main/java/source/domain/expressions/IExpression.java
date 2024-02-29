package source.domain.expressions;

import source.domain.adts.MyIDictionary;
import source.domain.adts.MyIHeap;
import source.domain.types.Type;
import source.exceptions.InterpreterException;
import source.domain.values.IValue;

public interface IExpression {
    IValue evaluate(MyIDictionary<String, IValue> symbolTable, MyIHeap heapTable, int threadID) throws InterpreterException;
    Type typeCheck(MyIDictionary<String, Type> typeTable) throws InterpreterException;
}
