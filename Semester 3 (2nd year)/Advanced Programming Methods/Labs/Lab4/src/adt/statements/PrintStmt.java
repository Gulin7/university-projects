package adt.statements;

import adt.ProgramState;
import adt.adts.MyIDictionary;
import adt.adts.MyIList;
import adt.expressions.Expression;
import adt.values.Value;
import controller.ExpressionEvaluationException;

public class PrintStmt implements IStmt{
    Expression expression;

    public PrintStmt(Expression expression) {
        this.expression = expression;
    }

    @Override
   public String toString()
   {
       return "print(" + expression.toString() + ");";
   }

    @Override
    public ProgramState execute(ProgramState state) throws ExpressionEvaluationException {
       MyIList<Value> output = state.getOutputList();
       MyIDictionary<String, Value> symbolTable = state.getSymbolTable();
       output.add(expression.evaluate(symbolTable));
       return state;
    }
}
