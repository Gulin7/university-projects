package source.domain.statements;

import source.domain.ProgramState;
import source.domain.adts.MyIDictionary;
import source.domain.types.Type;
import source.exceptions.InterpreterException;

public interface IStatement {
    ProgramState execute(ProgramState currentState) throws InterpreterException;
    MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeTable) throws InterpreterException;
}
