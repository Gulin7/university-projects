package com.example.a7_gui.model.program_statements;

import com.example.a7_gui.exceptions.DataStructureException;
import com.example.a7_gui.exceptions.ArithmeticException;
import com.example.a7_gui.exceptions.EvaluationException;
import com.example.a7_gui.exceptions.ExecutionException;
import com.example.a7_gui.model.program_expressions.IExpression;
import com.example.a7_gui.model.programState.ProgramState;
import com.example.a7_gui.model.program_expressions.OppositeExpression;
import com.example.a7_gui.model.program_expressions.VariableExpression;
import com.example.a7_gui.model.program_types.BoolType;
import com.example.a7_gui.model.program_types.Type;
import com.example.a7_gui.model.my_utils.MyIDictionary;
import com.example.a7_gui.model.my_utils.MyIStack;
import com.example.a7_gui.model.program_values.BoolValue;
import com.example.a7_gui.model.program_values.Value;


public class DoWhileStatement implements IStatement{
    private final IStatement innerStmt;
    private final IExpression condExpr;

    public DoWhileStatement(IExpression condExpr, IStatement stmt){
        this.innerStmt=stmt;
        this.condExpr=condExpr;
    }
    @Override
    public ProgramState execute(ProgramState state) throws ExecutionException, EvaluationException, DataStructureException, ArithmeticException{
        IStatement whileStmt = new CompoundStatement(innerStmt, new WhileStatement(condExpr, innerStmt));
        state.getExecutionStack().push(whileStmt);

        return null;
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws ExecutionException, EvaluationException, DataStructureException {
        Type typeExpr = condExpr.typeCheck(typeEnv);
        if(typeExpr.equals(new BoolType())){
            innerStmt.typeCheck(typeEnv.deepCopy());
            return typeEnv;
        }
        else{
            throw new ExecutionException("DoWhile: Condition must be of type bool");
        }
    }

    @Override
    public IStatement deepCopy() {
        return new DoWhileStatement(condExpr.deepCopy(), innerStmt.deepCopy());
    }

    @Override
    public String toString() {
        return String.format("do { %s } while ( %s )", innerStmt, condExpr);
    }
}
