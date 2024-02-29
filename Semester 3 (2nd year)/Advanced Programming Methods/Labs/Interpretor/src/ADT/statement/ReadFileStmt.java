package ADT.statement;

import ADT.PrgState;
import ADT.dictionary.MyIDictionary;
import ADT.expresion.Exp;
import ADT.heap.MyIHeap;
import ADT.stack.MyIStack;
import ADT.types.IntType;
import ADT.types.StringType;
import ADT.value.IntValue;
import ADT.value.StringValue;
import ADT.value.Value;
import Controller.MyException;

import java.io.BufferedReader;
import java.io.IOException;

public class ReadFileStmt implements IStmt{
    Exp exp_file_name;
    String var_name;
    public ReadFileStmt(Exp exp, String var_name){
        this.exp_file_name = exp;//string
        this.var_name = var_name;//int base
    }
    @Override
    public String toString(){
        return "readFile(file: " + exp_file_name + ", " + var_name + ");";
    }//TODO finish toString
    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIStack<IStmt> stk = state.getExeStack();
        MyIDictionary<String, BufferedReader> fileTable = state.getFileTable();
        MyIDictionary<String, Value> symTbl = state.getSymTable();
        MyIHeap<Value> heap = state.getHeap();
        Value val = symTbl.lookup(var_name);
        if (val == null) {
            throw new MyException("variable " + val.toString() + " not defined");
        }
        if (!val.getType().equals(new IntType())) {
            throw new MyException("variable " + val.toString() + " is not the required type- int");
        }
        Value expresionValue = exp_file_name.eval(symTbl, heap);
        if (!expresionValue.getType().equals(new StringType())) {
            throw new MyException("expresion " + expresionValue.toString() + " is not the required type- string");
        }
        //if (val.getType().equals(new StringType())) {
       //StringValue string_val = (StringValue) val;
//        fileTable.lookup(string_val.toString());//TODO do if( fileTable.lookup(string_val.toString()))
        BufferedReader reader = fileTable.lookup(expresionValue.toString());
        try {
            String line = reader.readLine();
            IntValue variableValue;
            if (line == null){
                variableValue = new IntValue(0);
            }
            else
                variableValue = new IntValue(Integer.parseInt(line));
            symTbl.put(var_name, variableValue);
        }
        catch (IOException ex) {
            throw new MyException(ex.getMessage());
        }
//        } else {
//            throw new MyException("Declared type of variable " + val.toString() + " and type of the assigned expression do not match ");
//        }
        return state;
    }
}
