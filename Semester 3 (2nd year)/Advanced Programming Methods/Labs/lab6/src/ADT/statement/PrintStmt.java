package ADT.statement;

import ADT.PrgState;
import ADT.dictionary.MyIDictionary;
import ADT.expresion.Exp;
import ADT.expresion.VarExp;
import ADT.heap.MyIHeap;
import ADT.list.MyIList;
import ADT.types.Type;
import ADT.value.Value;
import Controller.MyException;

public class PrintStmt implements IStmt{
    Exp exp;

    public PrintStmt(Exp expression) {
        this.exp = expression;
    }
    @Override
    public String toString(){ return "print(" +exp.toString()+")";}
    public PrgState execute(PrgState state) throws MyException{
        MyIList<Value> output = state.getOut();
        MyIDictionary<String, Value> symTable = state.getSymTable();
        MyIHeap<Value> heap = state.getHeap();
        Value value = exp.eval(symTable, heap);
        output.add(value);
        return null;
    }

    public MyIDictionary<String,Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException{
        exp.typecheck(typeEnv);
        return typeEnv;
    }
}