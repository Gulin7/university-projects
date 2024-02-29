package adt.statements;

import adt.ProgramState;
import adt.adts.MyIDictionary;
import adt.types.BoolType;
import adt.types.IntType;
import adt.types.StringType;
import adt.types.Type;
import adt.values.BoolValue;
import adt.values.IntValue;
import adt.values.StringValue;
import adt.values.Value;
import controller.StatementExecutionException;

public class VariableDeclarationStmt implements IStmt{
    String variableName;
    Type type;

    public VariableDeclarationStmt(String variableName, Type type) {
        this.variableName = variableName;
        this.type = type;
    }

    @Override
    public String toString(){
        return type.toString() + " " + variableName + ";";
    }

    @Override
    public ProgramState execute(ProgramState state) throws StatementExecutionException {
        MyIDictionary<String, Value> symbolTable = state.getSymbolTable();
        if (symbolTable.isDefined(variableName))
        {
            throw new StatementExecutionException("variable \"" + variableName + "\" is already declared");
        }
        else
        {
            if (type.equals(new IntType()))
            {
                Value intDefaultValue = new IntValue(0);
                symbolTable.put(variableName, intDefaultValue);
            }
            if (type.equals(new BoolType()))
            {
                Value boolDefaultValue = new BoolValue(false);
                symbolTable.put(variableName, boolDefaultValue);
            }
            if (type.equals(new StringType()))
            {
                Value stringDefaultValue = new StringValue("");
                symbolTable.put(variableName, stringDefaultValue);
            }
        }
        return state;
    }
}
