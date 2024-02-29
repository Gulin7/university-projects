package com.example.a7_gui.model.stmt;

import com.example.a7_gui.exceptions.ADTException;
import com.example.a7_gui.exceptions.DivisionByZero;
import com.example.a7_gui.exceptions.ExpressionEvaluationException;
import com.example.a7_gui.exceptions.StatementExecutionException;
import com.example.a7_gui.model.expressions.IExpression;
import com.example.a7_gui.model.programState.ProgramState;
import com.example.a7_gui.model.types.IntType;
import com.example.a7_gui.model.types.RefType;
import com.example.a7_gui.model.types.Type;
import com.example.a7_gui.model.utils.MyICountdownLatchTable;
import com.example.a7_gui.model.utils.MyIDictionary;
import com.example.a7_gui.model.utils.MyIHeap;
import com.example.a7_gui.model.values.IntValue;
import com.example.a7_gui.model.values.RefValue;
import com.example.a7_gui.model.values.Value;

public class HeapAllocationStmt implements IStatement{
    String variableName;
    IExpression expression;

    public HeapAllocationStmt(String variableName, IExpression expression){
        this.variableName = variableName;
        this.expression = expression;
    }

    @Override
    public IStatement deepCopy() {
        return new HeapAllocationStmt(variableName, expression.deepCopy());
    }

    @Override
    public String toString() {
        return "new(" + variableName + ", " + expression + ");";
    }

    @Override
    public ProgramState execute(ProgramState state) throws StatementExecutionException, ExpressionEvaluationException, ADTException, DivisionByZero {

        MyIDictionary<String, Value> symTable = state.getSymTable();
        MyIHeap heap = state.getHeap();

        if(!symTable.isDefined(variableName))
            throw new StatementExecutionException("Variable isn't defined!");

        Value varValue = symTable.lookUp(variableName);

        if(!(varValue.getType() instanceof RefType))
            throw new StatementExecutionException("Variable is not of type reference!");


        Value expressionValue = expression.eval(symTable, heap);

        if (!expressionValue.getType().equals(((RefType) varValue.getType()).getInner())) {
            throw new StatementExecutionException("Types not equal!");
        }

        int address = heap.getFreeValue();
        heap.add(expressionValue);
        symTable.update(variableName, new RefValue(address, expressionValue.getType()));

        return null;
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws StatementExecutionException, ExpressionEvaluationException, ADTException {
        Type typeVar = typeEnv.lookUp(variableName);
        Type typeExp = expression.typeCheck(typeEnv);
        if (typeVar.equals(new RefType(typeExp)))
            return typeEnv;
        throw new StatementExecutionException("NEW stmt: right hand side and left hand side have different types ");
    }

}
