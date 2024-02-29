package ADT.expresion;

import ADT.dictionary.MyIDictionary;
import ADT.heap.MyIHeap;
import ADT.types.Type;
import ADT.value.Value;
import Controller.MyException;

public interface Exp {
    Value eval(MyIDictionary<String,Value> tbl, MyIHeap<Value> heap) throws MyException;
    public String toString();
    Type typecheck(MyIDictionary<String, Type> typeEnv) throws MyException;
}