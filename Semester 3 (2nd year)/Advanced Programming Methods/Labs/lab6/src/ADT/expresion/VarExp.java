package ADT.expresion;

import ADT.dictionary.MyIDictionary;
import ADT.heap.MyIHeap;
import ADT.types.Type;
import ADT.value.Value;
import Controller.MyException;

public class VarExp implements Exp{
        String id;
        public VarExp(String v) {
                this.id = v;
        }
        @Override
        public String toString() {
                return  id;
        }
        public Value eval(MyIDictionary<String,Value> tbl, MyIHeap<Value> heap) throws MyException {
                if (!tbl.isDefined(id)) {
                        throw new MyException("Variable not found: " + id);
                }
                return tbl.lookup(id);
        }
        @Override
        public Type typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
                return typeEnv.lookup(id);
        }

}