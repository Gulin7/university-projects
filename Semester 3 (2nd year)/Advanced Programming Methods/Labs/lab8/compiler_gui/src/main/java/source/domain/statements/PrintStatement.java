package source.domain.statements;

import source.domain.ProgramState;
import source.domain.adts.MyIDictionary;
import source.domain.adts.MyIList;
import source.domain.expressions.IExpression;
import source.domain.types.Type;
import source.exceptions.InterpreterException;
import source.domain.values.IValue;

public class PrintStatement implements IStatement {
    private final IExpression expression;

    public PrintStatement(IExpression expression)
    {
        this.expression = expression;
    }

    /**
     * Executes a PrintStatement, adding the result of evaluating the expression to the output list.
     *
     * @param currentState The current program state.
     * @return The updated program state after executing the print statement.
     * @throws InterpreterException If there is an error during expression evaluation.
     */
    @Override
    public ProgramState execute(ProgramState currentState) throws InterpreterException {
        MyIList<IValue> outputList = currentState.getOutputList();

        outputList.add(expression.evaluate(
                currentState.getSymbolTable(),
                currentState.getHeapTable(),
                currentState.getId())
        );

        return null;
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeTable) throws InterpreterException {
        expression.typeCheck(typeTable);

        return typeTable;
    }

    @Override
    public String toString() {
        return "print(" + expression + ")";
    }
}
