package ADT.expresion;

import ADT.dictionary.MyIDictionary;
import ADT.heap.MyIHeap;
import ADT.types.BooleanType;
import ADT.types.IntType;
import ADT.types.Type;
import ADT.value.BoolValue;
import ADT.value.IntValue;
import ADT.value.Value;
import Controller.MyException;

public class RelationalExp implements Exp {
    Exp exp1;
    Exp exp2;
    String op;
    public RelationalExp(Exp exp1, String op, Exp exp2){
        this.exp1 = exp1;
        this.exp2 = exp2;
        this.op = op;
    }
    @Override
    public Value eval(MyIDictionary<String, Value> tbl, MyIHeap<Value> heap) throws MyException {
        Value v1 = exp1.eval(tbl, heap);
        Value v2 = exp2.eval(tbl,heap);
        if (!(v1 instanceof IntValue)) {
            throw new MyException("First operand is not an integer");
        }
        if (!(v2 instanceof IntValue)) {
            throw new MyException("Second operand is not an integer");
        }
        int n1 = ((IntValue) v1).getValue();
        int n2 = ((IntValue) v2).getValue();
        switch (op) {
            case "<":
                return new BoolValue(n1 < n2);
            case "<=":
                return new BoolValue(n1 <= n2);
            case "==":
                return new BoolValue(n1 == n2);
            case "!=":
               return new BoolValue(n1 != n2);
            case ">":
                return new BoolValue(n1 > n2);
            case ">=":
                return new BoolValue(n1 >= n2);
            default:
                throw new MyException("Invalid operand: " + op);
        }
    }
    @Override
    public String toString() {
        return exp1.toString() + op+exp2.toString();
    }
    public Type typecheck(MyIDictionary<String,Type> typeEnv) throws MyException{
        Type typ1, typ2;
        typ1=exp1.typecheck(typeEnv);
        typ2=exp2.typecheck(typeEnv);
        if (typ1.equals(new IntType())) {
            if (typ2.equals(new IntType())) {
                return new BooleanType();
            } else {
                throw new MyException("second operand is not an integer");
            }
        }else {
            throw new MyException("first operand is not an integer");
        }
    }
}
