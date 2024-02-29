package ADT.expresion;

import ADT.dictionary.MyIDictionary;
import ADT.heap.MyIHeap;
import ADT.types.Type;
import ADT.value.IntValue;
import ADT.value.Value;
import Controller.MyException;

public class ValueExp implements Exp{
    Value e;

    public ValueExp(Value value) {
        this.e= value;
    }
    @Override
    public Value eval(MyIDictionary<String,Value> tbl, MyIHeap<Value> heap) throws MyException{
        return e;
    }
    @Override
    public String toString(){
        return e.toString();
    }

    @Override
    public Type typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        return e.getType();
    }
}