package ADT.statement;

import ADT.PrgState;
import Controller.MyException;

public class NopStmt implements IStmt{
    @Override
    public PrgState execute(PrgState state) throws MyException {
        return state;
    }
    @Override
    public String toString(){
        return "Nop";
    }
}
