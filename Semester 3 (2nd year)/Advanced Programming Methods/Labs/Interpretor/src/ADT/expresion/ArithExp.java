package ADT.expresion;

import ADT.dictionary.MyIDictionary;
import ADT.heap.MyIHeap;
import ADT.value.IntValue;
import ADT.value.Value;
import Controller.MyException;

public class ArithExp implements Exp{
    Exp e1;
    Exp e2;
    char op; //1-plus, 2-minus, 3-star, 4-divide

    public ArithExp(char c, Exp ex1, Exp ex2) {
        op = c;
        e1 = ex1;
        e2 = ex2;
    }

    public Value eval(MyIDictionary<String, Value> tbl, MyIHeap<Value> heap) throws MyException {
        Value v1 = e1.eval(tbl, heap);
        Value v2 = e2.eval(tbl, heap);

        if (!(v1 instanceof IntValue)) {
            throw new MyException("First operand is not an integer");
        }
        if (!(v2 instanceof IntValue)) {
            throw new MyException("Second operand is not an integer");
        }

        int n1 = ((IntValue) v1).getValue();
        int n2 = ((IntValue) v2).getValue();

        switch (op) {
            case '+': // Addition
                return new IntValue(n1 + n2);
            case '-': // Subtraction
                return new IntValue(n1 - n2);
            case '*': // Multiplication
                return new IntValue(n1 * n2);
            case '/': // Division
                if (n2 == 0) {
                    throw new MyException("Division by zero");
                }
                return new IntValue(n1 / n2);
            default:
                throw new MyException("Invalid operation code");
        }
    }
    @Override
    public String toString() {
        return "(" + e1.toString() + " " + op + " " + e2.toString() + ")";
    }
}
