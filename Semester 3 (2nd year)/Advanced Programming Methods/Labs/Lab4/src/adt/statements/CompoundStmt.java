package adt.statements;

import adt.ProgramState;
import adt.adts.MyIStack;

public class CompoundStmt implements IStmt{
    IStmt firstStmt;
    IStmt secondStmt;

    public CompoundStmt(IStmt firstStmt, IStmt secondStmt) {
        this.firstStmt = firstStmt;
        this.secondStmt = secondStmt;
    }

    @Override
    public String toString() {
        return "(" + firstStmt.toString() + "\n" + secondStmt.toString() + ")";
    }

    @Override
    public ProgramState execute(ProgramState state) {
        MyIStack<IStmt> stack = state.getExecutionStack();
        stack.push(secondStmt);
        stack.push(firstStmt);
        return state;
    }
}
