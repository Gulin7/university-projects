package ADT.statement;

import ADT.PrgState;
import ADT.dictionary.MyIDictionary;
import ADT.types.Type;
import Controller.MyException;

import java.io.FileNotFoundException;
import java.io.IOException;

public interface IStmt{
    //PrgState execute(PrgState state) throws MyException;
    //which is the execution method for a statement.
    PrgState execute(PrgState state) throws MyException;
    MyIDictionary<String, Type> typecheck(MyIDictionary<String,Type> typeEnv) throws MyException;
}