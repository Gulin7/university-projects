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

import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.Files;
import java.io.BufferedReader;
import java.io.IOException;

import java.io.FileNotFoundException;
import java.io.FileReader;

public class OpenRFileStmt implements IStmt{
    Exp exp;
    public OpenRFileStmt(Exp exp){
        this.exp = exp;
    }
    @Override
    public PrgState execute(PrgState state) throws MyException{
        MyIStack<IStmt> stk = state.getExeStack();
        MyIDictionary<String, BufferedReader> fileTable = state.getFileTable();
        MyIDictionary<String, Value> symTbl = state.getSymTable();
        MyIHeap<Value> heap = state.getHeap();
        Value val = exp.eval(symTbl, heap);
        if(val.getType().equals(new StringType())){
            StringValue string_path = (StringValue)val;
            if(symTbl.isDefined(string_path.getVal())){
                throw new MyException("Declared variable already exists.");
            }
            try{
                Path filePath = Paths.get(string_path.toString());
                BufferedReader reader = Files.newBufferedReader(filePath);
                fileTable.put(string_path.toString(),reader);//TODO check if it already exists
            }catch(IOException ex){
                throw new MyException(ex.getMessage());
            }
        }
        else{
            throw new MyException("Declared type of variable " + val.toString() + " and type of the assigned expression do not match ");
        }
        return state;
    }
    @Override
    public String toString(){
        return "open file( " + this.exp.toString() + " ) ";
    }
}
