package ADT.expresion;

import ADT.dictionary.MyIDictionary;
import ADT.heap.MyIHeap;
import ADT.types.BooleanType;
import ADT.types.IntType;
import ADT.types.Type;
import ADT.value.BoolValue;
import ADT.value.Value;
import Controller.MyException;

public class LogicExp implements Exp {
    private static final int AND = 1;
    private static final int OR = 2;
    Exp e1;
    Exp e2;
    int op; // 1 for 'and', 2 for 'or'
    public LogicExp(char c, Exp ex1, Exp ex2) {
        op = c;
        e1 = ex1;
        e2 = ex2;
    }
    public Value eval(MyIDictionary<String, Value> tbl, MyIHeap<Value> heap) throws MyException {
        Value v1 = e1.eval(tbl, heap);
        Value v2 = e2.eval(tbl, heap);
        if (!(v1 instanceof BoolValue) || !(v2 instanceof BoolValue)) {
            throw new MyException("Operands of 'and' must be boolean");
        }
        boolean b1 = ((BoolValue) v1).getValue();
        boolean b2 = ((BoolValue) v2).getValue();
        if (op == 1) { // Logical AND
            return new BoolValue(b1 && b2);
        } else if (op == 2) { // Logical OR
            return new BoolValue(b1 || b2);
        } else {
            throw new MyException("Invalid operation code");
        }
    }
    @Override
    public String toString() {
        switch (op) {
            case AND:
                return "(" + e1 + ") AND (" + e2 + ")";
            case OR:
                return "(" + e1 + ") OR (" + e2 + ")";
            default:
                return "Invalid expression.";
        }
    }

    public Type typecheck(MyIDictionary<String,Type> typeEnv) throws MyException{
        Type typ1, typ2;
        typ1=e1.typecheck(typeEnv);
        typ2=e2.typecheck(typeEnv);
        if (typ1.equals(new BooleanType())) {
            if (typ2.equals(new BooleanType())) {
                return new BooleanType();
            } else {
                throw new MyException("second operand is not a boolean");
            }
        }else {
            throw new MyException("first operand is not a boolean");
        }
    }
}






