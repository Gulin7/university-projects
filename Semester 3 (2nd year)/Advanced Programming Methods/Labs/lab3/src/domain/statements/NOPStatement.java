package domain.statements;

import domain.ProgramState;

public class NOPStatement implements IStatement {
    @Override
    public ProgramState execute(ProgramState currentState) {
        return currentState;
    }

    @Override
    public String toString() {
        return "(NOP)";
    }
}
