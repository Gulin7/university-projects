package adt.statements;

import adt.ProgramState;
import adt.adts.MyIDictionary;
import adt.adts.MyIStack;
import adt.expressions.Expression;
import adt.types.Type;
import adt.values.Value;
import controller.ExpressionEvaluationException;
import controller.StatementExecutionException;

public class AssignmentStmt implements IStmt{
    String variableName;
    Expression expression;

    public AssignmentStmt(String variableName, Expression expression) {
        this.variableName = variableName;
        this.expression = expression;
    }

    @Override
    public String toString() {
        return variableName+" = "+ expression.toString() + ";";
    }

    @Override
    public ProgramState execute(ProgramState state) throws ExpressionEvaluationException, StatementExecutionException{
        MyIDictionary<String, Value> symTable = state.getSymbolTable();
        if (symTable.isDefined(variableName))
        {
            Value expressionValue = expression.evaluate(symTable);
            Type variableType = (symTable.lookUp(variableName)).getType();
            if (expressionValue.getType().equals(variableType))
            {
                symTable.update(variableName, expressionValue);
            }
            else throw new StatementExecutionException("declared type of variable "+variableType+" and type of " +
                    "the assigned expression do not match");
        }
        else throw new StatementExecutionException("the used variable " + variableName + " was not declared before");
        return state;
    }
}
