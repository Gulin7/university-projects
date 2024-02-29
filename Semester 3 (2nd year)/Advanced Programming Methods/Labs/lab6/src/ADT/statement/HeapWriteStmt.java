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

public class HeapWriteStmt implements IStmt{
    String var_name;
    Exp exp;
    public HeapWriteStmt(String var_name, Exp exp){
        this.exp = exp;
        this.var_name = var_name;
    }
    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIStack<IStmt> stk = state.getExeStack();
        MyIDictionary<String, Value> symTbl = state.getSymTable();
        MyIHeap<Value> heap = state.getHeap();
        if(!symTbl.isDefined(var_name)){
            throw new MyException(var_name + "was not defined before");
        }
        Value var_name_value = symTbl.lookup(var_name);
        if(!(var_name_value.getType() instanceof RefType)){
            throw new MyException(var_name + " its not of type RefType");
        }
        RefValue ref_val = (RefValue) var_name_value;
        int heap_address = ref_val.getAddr();
        if(!heap.isDefined(heap_address)){
            throw new MyException(var_name + "not defined in the hep table");
        }
        Value exp_val = exp.eval(symTbl, heap);
        RefType var_name_type = (RefType) var_name_value.getType();
        Type inner_type =  var_name_type.getInner();
        if(!(exp_val.getType().equals(inner_type))){
            throw new MyException("inner type val does not match ref declaratio type");
        }
        heap.update(heap_address, exp_val);
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type typeVar = typeEnv.lookup(var_name);
        Type typeExp = exp.typecheck(typeEnv);
        if (typeVar.equals(new RefType(typeExp)))
            return typeEnv;
        else
            throw new MyException("HEAP WRITE STMT: var_name" + var_name + " and exp"+ exp +"have different types ");
    }

    @Override
    public String toString(){
        return "wH(" + var_name + ','+ exp +')';
    }
}
