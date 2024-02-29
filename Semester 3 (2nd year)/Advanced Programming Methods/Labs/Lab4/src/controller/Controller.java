package controller;

import adt.statements.IStmt;
import adt.adts.MyIStack;
import adt.ProgramState;
import repository.IRepository;

import java.io.IOException;

public class Controller {
    private final IRepository repository;

    public Controller(IRepository repository) {
        this.repository = repository;
    }

    public ProgramState oneStep(ProgramState state) throws ExpressionEvaluationException, StatementExecutionException, IOException {
        MyIStack<IStmt> stack=state.getExecutionStack();
        if(stack.isEmpty()) throw new ExpressionEvaluationException("Program state stack is empty");
        IStmt currentStmt = stack.pop();
        return currentStmt.execute(state);
    }

    public void allSteps(int displayFlag) throws ExpressionEvaluationException, StatementExecutionException, IOException {
        ProgramState program = repository.getCrtPrg(0);
        if (displayFlag == 1)
            System.out.println(program);
        repository.logProgramStateExecution();
        while (!program.getExecutionStack().isEmpty()){
            oneStep(program);
            if (displayFlag == 1)
                System.out.println(program);
            repository.logProgramStateExecution();
        }
    }
}
