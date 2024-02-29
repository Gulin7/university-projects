package source.domain.statements;

import source.domain.ProgramState;
import source.domain.adts.MyIDictionary;
import source.domain.types.Type;
import source.exceptions.InterpreterException;

public class NOPStatement implements IStatement {
    @Override
    public ProgramState execute(ProgramState currentState) {
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeTable) throws InterpreterException {
        return typeTable;
    }

    @Override
    public String toString() {
        return "NOP";
    }
}
