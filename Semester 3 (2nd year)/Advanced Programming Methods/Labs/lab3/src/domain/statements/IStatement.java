package domain.statements;

import domain.ProgramState;
import exceptions.ExpressionException;
import exceptions.InterpreterException;
import exceptions.StatementException;
import domain.ProgramState;

public interface IStatement {
    ProgramState execute(ProgramState currentState) throws StatementException, ExpressionException, InterpreterException;
}
