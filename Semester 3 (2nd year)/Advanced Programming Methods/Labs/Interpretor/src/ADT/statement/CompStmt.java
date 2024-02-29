package ADT.statement;


import ADT.PrgState;
import ADT.stack.MyIStack;
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
        return state;
    }
}
