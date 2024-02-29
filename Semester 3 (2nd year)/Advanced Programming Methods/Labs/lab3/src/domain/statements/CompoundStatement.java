package domain.statements;

import exceptions.ExpressionException;
import domain.utils.MyIStack;
import domain.ProgramState;

public class CompoundStatement implements IStatement {
    private final IStatement firstStatement, secondStatement;

    public CompoundStatement(IStatement firstStatement, IStatement secondStatement)
    {
        this.firstStatement = firstStatement;
        this.secondStatement = secondStatement;
    }

    public IStatement getFirstStatement()
    {
        return this.firstStatement;
    }

    public IStatement getSecondStatement()
    {
        return this.secondStatement;
    }

    @Override
    public String toString() {
        return firstStatement.toString() + ";" + secondStatement.toString();
    }

    @Override
    public ProgramState execute(ProgramState currentState) throws ExpressionException {
        MyIStack<IStatement> exeStack = currentState.getStack();

        exeStack.push(secondStatement);
        exeStack.push(firstStatement);

        return currentState;
    }
}
