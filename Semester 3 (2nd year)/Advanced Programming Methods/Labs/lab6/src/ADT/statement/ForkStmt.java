package ADT.statement;

import ADT.PrgState;
import ADT.dictionary.MyDictionary;
import ADT.dictionary.MyIDictionary;
import ADT.stack.MyIStack;
import ADT.stack.MyStack;
import ADT.types.RefType;
import ADT.types.Type;
import ADT.value.Value;
import Controller.MyException;

import java.util.Map;

public class ForkStmt implements IStmt{
    IStmt statement;
    public ForkStmt(IStmt stmt) { statement = stmt;}
    @Override
    public PrgState execute(PrgState program){
        MyIStack<IStmt> forkExecution = new MyStack<IStmt>();
        MyIDictionary<String, Value> cloneSym = new MyDictionary<String,Value>();
        for (Map.Entry<String,Value> var: program.getSymTable().getMap().entrySet())
            cloneSym.put(var.getKey(), var.getValue());
        PrgState forkProgram = new PrgState(forkExecution, cloneSym, program.getOut(), statement,program.getFileTable(), program.getHeap());
        return forkProgram;
    }
    @Override
    public String toString() { return "fork(" + statement + ");"; }

    public MyIDictionary<String, Type> typecheck(MyIDictionary<String,Type> typeEnv) throws MyException{
        return statement.typecheck(typeEnv.clone());
    }
}
