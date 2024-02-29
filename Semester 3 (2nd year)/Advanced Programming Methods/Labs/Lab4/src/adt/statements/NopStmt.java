package adt.statements;

import adt.ProgramState;

public class NopStmt implements IStmt{
    public ProgramState execute(ProgramState state)
    {
        return state;
    }
}
