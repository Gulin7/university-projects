package ADT.statement;

import ADT.PrgState;
import ADT.dictionary.MyIDictionary;
import ADT.stack.MyIStack;
import ADT.types.IntType;
import ADT.types.RefType;
import ADT.value.BoolValue;
import ADT.value.IntValue;
import ADT.value.Value;
import Controller.MyException;
import ADT.types.Type;

import java.util.Objects;

public class VarDeclStmt implements IStmt{
    String name;
    Type type;

    public VarDeclStmt(String name, Type type) {
        this.name = name;
        this.type = type;
    }
    public String toString() {
        return " " + type + " " + name;
    }
    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIDictionary<String, Value> symTable = state.getSymTable();
        MyIStack<IStmt> exeStack = state.getExeStack();

        if (symTable.isDefined(name)) {
            throw new MyException("Variable is already declared: " + name);
        } else {
            if (Objects.equals(type.toString(), "int") || Objects.equals(type.toString(), "string") ||
                    Objects.equals(type.toString(), "boolean") || type instanceof RefType) {
                symTable.put(name, type.defaultValue());
            }
            else{
                throw new MyException("Unsupported variable type: " + type.toString());
            }
        }
        return null;
    }
    public MyIDictionary<String,Type> typecheck(MyIDictionary<String,Type> typeEnv) throws MyException{
        typeEnv.put(name, type);
        return typeEnv;
    }

}