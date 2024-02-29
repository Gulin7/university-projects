package ADT.statement;

import ADT.PrgState;
import ADT.dictionary.MyIDictionary;
import ADT.expresion.Exp;
import ADT.expresion.ValueExp;
import ADT.heap.MyIHeap;
import ADT.stack.MyIStack;
import ADT.value.Value;
import Controller.MyException;
import ADT.types.Type;
public class AssignStmt implements IStmt {
    String id;
    Exp exp;

    public AssignStmt(String variableName, Exp valueExp) {
        this.id = variableName;
        this.exp = valueExp;
    }

    public String toString() {
        return id + "=" + exp.toString();
    }

    public PrgState execute(PrgState state) throws MyException {
        MyIStack<IStmt> stk = state.getExeStack();
        MyIDictionary<String, Value> symTbl = state.getSymTable();
        MyIHeap<Value> heap = state.getHeap();
        if (symTbl.isDefined(id)) {
            Value val = exp.eval(symTbl, heap);
            Type typId = (symTbl.lookup(id)).getType();
            if (val.getType().equals(typId)) {
                symTbl.update(id, val);
            } else
                throw new MyException("declared type of variable" + id + " and type of the assigned expression do not match ");

        } else {
            throw new MyException("the used variable" + id + " was not declared before");
        }
        return null;
    }
    public MyIDictionary<String,Type> typecheck(MyIDictionary<String,Type> typeEnv) throws MyException{
        Type typeVar = typeEnv.lookup(id);
        Type typeExp = exp.typecheck(typeEnv);
        if (typeVar.equals(typeExp))
            return typeEnv;
        else
            throw new MyException("Assignment: right hand side" + id + typeVar+ " and left hand side"+ exp +"have different types ");
    }
}