package controller;

import exceptions.ExpressionException;
import exceptions.InterpreterException;
import exceptions.StackException;
import exceptions.StatementException;
import repository.IRepository;
import domain.statements.IStatement;
import domain.utils.MyIStack;
import domain.ProgramState;
import repository.ProgramsRepository;

import java.util.Stack;

public class Controller {
    private final IRepository programs;

    public Controller(IRepository programs)
    {
        this.programs = programs;
    }

    public void addProgram(ProgramState programToAdd)
    {
        programs.addProgram(programToAdd);
    }

    public ProgramState getCurrentProgram()
    {
        return programs.getCurrentProgram();
    }

    public boolean isEmpty()
    {
        return this.programs.getCurrentProgram().getStack().isEmpty();
    }

    public ProgramState executeOneStatement(ProgramState currentState) throws StatementException, ExpressionException, StackException {
        MyIStack<IStatement> exeStack = currentState.getStack();

        try {
            IStatement currentStatement = exeStack.pop();
            return currentStatement.execute(currentState);
        }
        catch (StackException | InterpreterException e)
        {
            throw new StatementException("Statements stack is empty!");
        }
    }

    public void executeAllStatements() throws StatementException, ExpressionException, StackException
    {
        ProgramState currentState = ProgramsRepository.getCurrentProgram();

        while (!currentState.getStack().isEmpty())
        {
            this.executeOneStatement(currentState);
            this.programs.logProgramState();
        }
    }
}
