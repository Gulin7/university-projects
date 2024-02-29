package ADT.statement;

import ADT.PrgState;
import Controller.MyException;

import java.io.FileNotFoundException;
import java.io.IOException;

public interface IStmt{
    //PrgState execute(PrgState state) throws MyException;
    //which is the execution method for a statement.
    PrgState execute(PrgState state) throws MyException;
}