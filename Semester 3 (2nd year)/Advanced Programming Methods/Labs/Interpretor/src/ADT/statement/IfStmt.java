package ADT.statement;

import ADT.PrgState;
import ADT.dictionary.MyIDictionary;
import ADT.expresion.Exp;
import ADT.heap.MyIHeap;
import ADT.stack.MyIStack;
import ADT.value.BoolValue;
import ADT.value.Value;
import Controller.MyException;

public class IfStmt implements IStmt {
    Exp exp;
    IStmt thenS;
    IStmt elseS;
    public IfStmt(Exp e, IStmt t, IStmt el) {
        exp = e;
        thenS = t;
        elseS = el;
    }
    public String toString() {
        return "(IF(" + exp.toString() + ") THEN(" + thenS.toString()
                + ")ELSE(" + elseS.toString() + "))";
    }
    public PrgState execute(PrgState state) throws MyException {
        MyIDictionary<String, Value> symTable = state.getSymTable();
        MyIStack<IStmt> exeStack = state.getExeStack();
        MyIHeap<Value> heap = state.getHeap();
        // Evaluate the condition
        Value conditionValue = exp.eval(symTable, heap);
        if (!(conditionValue instanceof BoolValue)) {
            throw new MyException("Conditional expression is not a boolean");
        }

        // If cond true, push 'thenS' on stack otherwise push 'elseS'
        if (((BoolValue) conditionValue).getValue()) {
            exeStack.push(thenS);
        } else {
            exeStack.push(elseS);
        }
        return state;
    }
}