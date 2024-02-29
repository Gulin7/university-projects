package domain.statements;

import exceptions.ExpressionException;
import domain.dataTypes.IValue;
import domain.utils.MyIList;
import domain.ProgramState;
import domain.expressions.IExpression;

public class PrintStatement implements IStatement {
    private final IExpression expression;

    public PrintStatement(IExpression expression)
    {
        this.expression = expression;
    }

    @Override
    public ProgramState execute(ProgramState currentState) throws ExpressionException {
        MyIList<IValue> outputList = currentState.getOutputList();

        outputList.add(expression.evaluateExpression(currentState.getSymbolTable()));

        return currentState;
    }

    @Override
    public String toString() {
        return "(print " + expression + ")";
    }
}