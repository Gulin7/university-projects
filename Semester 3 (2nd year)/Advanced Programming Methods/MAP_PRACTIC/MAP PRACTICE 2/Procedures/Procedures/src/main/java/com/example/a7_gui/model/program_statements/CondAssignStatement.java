package com.example.a7_gui.model.program_statements;

import com.example.a7_gui.exceptions.DataStructureException;
import com.example.a7_gui.exceptions.ArithmeticException;
import com.example.a7_gui.exceptions.EvaluationException;
import com.example.a7_gui.exceptions.ExecutionException;
import com.example.a7_gui.model.program_expressions.IExpression;
import com.example.a7_gui.model.programState.ProgramState;
import com.example.a7_gui.model.program_expressions.VariableExpression;
import com.example.a7_gui.model.program_types.BoolType;
import com.example.a7_gui.model.program_types.Type;
import com.example.a7_gui.model.my_utils.MyIDictionary;
import com.example.a7_gui.model.my_utils.MyIStack;
import com.example.a7_gui.model.program_values.BoolValue;
import com.example.a7_gui.model.program_values.Value;

public class CondAssignStatement implements IStatement {
    private final IExpression expr1;
    private final IExpression expr2;
    private final IExpression expr3;
    private final String variable;

    public CondAssignStatement(IExpression expr1, IExpression expr2, IExpression expr3, String var)
    {
        this.expr1=expr1;
        this.expr2=expr2;
        this.expr3=expr3;
        this.variable=var;
    }

    @Override
    public ProgramState execute(ProgramState state) throws ExecutionException, EvaluationException, DataStructureException, ArithmeticException{
        MyIStack<IStatement> exeStack = state.getExecutionStack();
        IStatement ifStatement = new IfStatement(expr1, new AssignStatement(variable, expr2), new AssignStatement(variable, expr3));

        exeStack.push(ifStatement);
        state.setExeStack(exeStack);

        return null;
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws ExecutionException, EvaluationException, DataStructureException {
        Type varType = new VariableExpression(this.variable).typeCheck(typeEnv);
        Type type1 = expr1.typeCheck(typeEnv);
        Type type2 = expr2.typeCheck(typeEnv);
        Type type3 = expr3.typeCheck(typeEnv);

        if(type1.equals(new BoolType()) && type2.equals(varType) && type3.equals(varType))
            return typeEnv;
        else throw new ExecutionException("CondAssignStmt: One of the expressions has no compatible tupe");
    }

    @Override
    public IStatement deepCopy() {
        return new CondAssignStatement(expr1.deepCopy(), expr2.deepCopy(), expr3.deepCopy(), variable);
    }

    @Override
    public String toString() {
        return String.format("%s = (%s) ? %s : %s", this.variable, this.expr1, this.expr2, this.expr3);
    }
}
