package source.domain.statements;

import source.domain.ProgramState;
import source.domain.adts.MyIDictionary;
import source.domain.adts.MyIStack;
import source.domain.adts.MyStack;
import source.domain.types.Type;
import source.exceptions.InterpreterException;

public class ForkStatement implements IStatement {
    private final IStatement innerStatement;

    public ForkStatement(IStatement innerStatement)
    {
        this.innerStatement = innerStatement;
    }

    @Override
    public ProgramState execute(ProgramState currentState) throws InterpreterException {
        MyIStack<IStatement> newThreadStack = new MyStack<>();
        newThreadStack.push(innerStatement);

        return new ProgramState(newThreadStack, currentState.getSymbolTable().copy(), currentState.getOutputList(),
                currentState.getFileTable(), currentState.getHeapTable());
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeTable) throws InterpreterException {
        innerStatement.typeCheck(typeTable.copy());

        return typeTable;
    }

    @Override
    public String toString() {
        return "Fork(" + innerStatement + ")";
    }
}
