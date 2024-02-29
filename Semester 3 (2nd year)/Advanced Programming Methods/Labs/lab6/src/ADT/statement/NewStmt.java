package ADT.statement;

import ADT.PrgState;
import ADT.dictionary.MyIDictionary;
import ADT.expresion.Exp;
import ADT.heap.MyIHeap;
import ADT.stack.MyIStack;
import ADT.types.RefType;
import ADT.types.Type;
import ADT.value.RefValue;
import ADT.value.Value;
import Controller.MyException;

public class NewStmt implements IStmt{
    private String var_name;
    private Exp exp;
    public NewStmt(String var_name, Exp exp){
        this.var_name = var_name;
        this.exp = exp;
    }
    @Override
    public String toString() {
        return "new(" + var_name + ", " + exp.toString() +')';
    }
    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIStack<IStmt> stk = state.getExeStack();
        MyIDictionary<String, Value> symTbl = state.getSymTable();
        MyIHeap<Value> heap = state.getHeap();
        if(!symTbl.isDefined(var_name)) {
            throw new MyException("the used variable" + var_name + " was not declared before");
        }
        Value val1 = symTbl.lookup(var_name);
        if(!(val1.getType() instanceof RefType)){
            throw new MyException("Exp" + exp + "is not of type Ref");
        }
        RefValue reference = (RefValue)val1;
        Value exp_val = exp.eval(symTbl, heap);
        RefType refType = (RefType) reference.getType();
        Type locationType = refType.getInner();
        if(exp_val.getType().equals(locationType)) {
            int indexToBeRemovedFromHeap = reference.getAddr();
            heap.delete(indexToBeRemovedFromHeap);
            int index = heap.getFreeIndex();
            heap.put(exp_val);
            reference.setAddress(index);
            symTbl.put(var_name, new RefValue(index, locationType));
        }
        else{
            throw new MyException(exp + "type does not match" + var_name + "type");
        }
        return null;
    }
    public MyIDictionary<String,Type> typecheck(MyIDictionary<String,Type> typeEnv) throws MyException{
        Type typeVar = typeEnv.lookup(var_name);
        Type typeExp = exp.typecheck(typeEnv);
        if (typeVar.equals(new RefType(typeExp)))
            return typeEnv;
        else
            throw new MyException("NEW stmt: right hand side and left hand side have different types ");
    }
}
