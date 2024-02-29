package adt.statements;

import adt.ProgramState;
import controller.ExpressionEvaluationException;
import controller.StatementExecutionException;

import java.io.IOException;

public interface IStmt {
    ProgramState execute(ProgramState state) throws ExpressionEvaluationException, StatementExecutionException, IOException;
}
