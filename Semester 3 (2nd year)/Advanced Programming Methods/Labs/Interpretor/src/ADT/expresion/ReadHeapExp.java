package ADT.expresion;

import ADT.dictionary.MyIDictionary;
import ADT.heap.MyIHeap;
import ADT.types.RefType;
import ADT.value.RefValue;
import ADT.value.Value;
import Controller.MyException;

public class ReadHeapExp implements Exp{
    Exp exp;
    public ReadHeapExp(Exp exp){
        this.exp = exp;
    }
    @Override
    public Value eval(MyIDictionary<String, Value> tbl, MyIHeap<Value> heap) throws MyException {
        Value val = exp.eval(tbl, heap);
        if(!(val.getType() instanceof RefType)){
            throw  new MyException("exp" + exp + "it's not an RefType");
        }
        RefValue ref_val = (RefValue)val;
        int index = ref_val.getAddr();
        if(!heap.isDefined(index)){
            throw new MyException(exp + "it's not defined in heap table");
        }
        //Value refValue = (Value) ((RefType) val.getType()).getInner();
        //RefType refType = (RefType) ref_val.getType();
        Value returnVal = heap.lookup(index);
        return returnVal;
    }
    @Override
    public String toString(){
        return "rH(" + exp + ')';
    }
}
