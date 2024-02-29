package ADT.statement;

import ADT.PrgState;
import ADT.dictionary.MyIDictionary;
import ADT.types.Type;
import Controller.MyException;

public class NopStmt implements IStmt{
    @Override
    public PrgState execute(PrgState state) throws MyException {
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        return typeEnv;
    }

    @Override
    public String toString(){
        return "Nop";
    }
}
