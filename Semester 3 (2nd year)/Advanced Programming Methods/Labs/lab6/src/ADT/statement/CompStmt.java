package ADT.statement;


import ADT.PrgState;
import ADT.dictionary.MyIDictionary;
import ADT.stack.MyIStack;
import ADT.types.Type;
import Controller.MyException;

public class CompStmt implements IStmt {
    IStmt first;
    IStmt snd;

    public CompStmt(IStmt first, IStmt second) {
        this.first=first;
        this.snd=second;
    }

    @Override
    public String toString() {
        return "("+first.toString() + ";" + snd.toString()+")";
    }
    public PrgState execute(PrgState state) throws MyException {
       // MyIStack<IStmt> stk=state.getStk();
        MyIStack<IStmt> stk=state.getExeStack();
        stk.push(snd);
        stk.push(first);
        return null;
    }

    public MyIDictionary<String, Type> typecheck(MyIDictionary<String,Type> typeEnv) throws MyException{
        return snd.typecheck(first.typecheck(typeEnv));
    }
}
