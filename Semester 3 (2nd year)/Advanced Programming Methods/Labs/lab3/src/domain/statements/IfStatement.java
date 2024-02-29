package domain.statements;

import domain.ProgramState;
import exceptions.ExpressionException;
import domain.*;
import domain.expressions.IExpression;
import domain.dataTypes.BoolType;
import domain.dataTypes.BoolValue;
import domain.dataTypes.IValue;
import domain.utils.MyIStack;

public class IfStatement implements IStatement {
    private final IExpression expressionToEvaluate;
    private final IStatement firstStatement, secondStatement;

    public IfStatement(IExpression expressionToEvaluate, IStatement firstStatement, IStatement secondStatement)
    {
        this.expressionToEvaluate = expressionToEvaluate;
        this.firstStatement = firstStatement;
        this.secondStatement = secondStatement;
    }

    @Override
    public ProgramState execute(ProgramState currentState) throws ExpressionException {
        MyIStack<IStatement> exeStack = currentState.getStack();

        IValue conditionToEvaluate = expressionToEvaluate.evaluateExpression(currentState.getSymbolTable());

        if (!conditionToEvaluate.getType().equals(new BoolType()))
            throw new ExpressionException("Conditional expression is not boolean!");

        BoolValue conditionValue = (BoolValue) conditionToEvaluate;

        if (conditionValue.getValue())
            exeStack.push(firstStatement);
        else
            exeStack.push(secondStatement);

        return currentState;
    }

    @Override
    public String toString() {
        return "(if " + expressionToEvaluate + " then " + firstStatement
                + " else " + secondStatement + ")";
    }
}