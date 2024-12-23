package ADT.statement;

import ADT.PrgState;
import ADT.dictionary.MyIDictionary;
import ADT.expresion.Exp;
import ADT.heap.MyIHeap;
import ADT.stack.MyIStack;
import ADT.types.BooleanType;
import ADT.value.BoolValue;
import ADT.value.Value;
import Controller.MyException;

public class WhileStmt implements IStmt{
    private Exp exp;
    private IStmt stmt;
    public WhileStmt(Exp exp, IStmt stmt){
        this.exp = exp;
        this.stmt = stmt;
    }
    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIStack<IStmt> stk = state.getExeStack();
        MyIDictionary<String, Value> symTbl = state.getSymTable();
        MyIHeap<Value> heap = state.getHeap();
        Value val = exp.eval(symTbl, heap);
        if(!(val.getType() instanceof BooleanType)){
            throw new MyException(exp + "it's not boolean type");
        }
        BoolValue boolValue = (BoolValue)val;
        if(boolValue.getValue()){
            stk.push(new WhileStmt(exp,stmt));
            stk.push(stmt);
        }
        return null;
    }
    @Override
    public String toString(){
        return "while(" + exp +"){" + stmt +"}";
    }
}
