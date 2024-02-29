package repository;

import adt.ProgramState;
import controller.ExpressionEvaluationException;
import controller.StatementExecutionException;

import java.io.IOException;

public interface IRepository {
    ProgramState getCrtPrg(int index);
    void add(ProgramState e);
    void logProgramStateExecution() throws IOException;
}
