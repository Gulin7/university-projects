package ADT.statement;

import ADT.PrgState;
import ADT.dictionary.MyIDictionary;
import ADT.expresion.Exp;
import ADT.heap.MyIHeap;
import ADT.stack.MyIStack;
import ADT.types.StringType;
import ADT.value.StringValue;
import ADT.value.Value;
import Controller.MyException;

import java.io.BufferedReader;
import java.io.IOException;

public class CloseRFileStmt implements IStmt{
    Exp exp;
    public CloseRFileStmt(Exp exp){
        this.exp = exp;
    }
    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIStack<IStmt> stk = state.getExeStack();
        MyIDictionary<String, BufferedReader> fileTable = state.getFileTable();
        MyIDictionary<String, Value> symTbl = state.getSymTable();
        MyIHeap<Value> heap = state.getHeap();
        Value val = exp.eval(symTbl, heap);
        if (val.getType().equals(new StringType())) {
            StringValue string_val = (StringValue) val;
            if(fileTable.isDefined(string_val.toString())){
                try {
                    BufferedReader reader = fileTable.lookup(string_val.toString());
                    reader.close();
                }
                catch (IOException ex){
                    throw new MyException(ex.getMessage());
                }
                fileTable.delete(string_val.toString());
            }
            else{
                throw new MyException("file not found");
            }
        }
        else {
            throw new MyException("Declared type of variable " + val.toString() + " and type of the assigned expression do not match ");
        }
        return state;
    }

    @Override
    public String toString(){
        return "closed file( " + this.exp.toString() + " ) ";
    }
}
