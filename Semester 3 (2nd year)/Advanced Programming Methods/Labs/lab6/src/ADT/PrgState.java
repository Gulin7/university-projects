package ADT;

import ADT.heap.MyIHeap;
import ADT.statement.IStmt;
import ADT.value.Value;
import ADT.dictionary.MyIDictionary;
import ADT.list.MyIList;
import ADT.stack.MyIStack;
import Controller.MyException;

import java.io.BufferedReader;
import java.util.Iterator;


public class PrgState {
    private static int globalId = 0;
    int currentId;
    MyIStack<IStmt> exeStack;
    MyIDictionary<String, Value> symTable;
    MyIList<Value> out;
    MyIDictionary<String, BufferedReader> fileTable;
    MyIHeap<Value> heap;
    IStmt originalProgram;

    public synchronized int incrementID() {
        globalId++;
        return globalId;
    }

    public int getCurrentId() {
        return this.currentId;
    }

    public int getGlobalID() {
        return globalId;
    }

    public PrgState(MyIStack<IStmt> stk, MyIDictionary<String, Value> symtbl, MyIList<Value> out, IStmt prg,
                    MyIDictionary<String, BufferedReader> fileTable, MyIHeap<Value> heap) {
        this.exeStack = stk;
        this.symTable = symtbl;
        this.out = out;
        this.fileTable = fileTable;
        this.heap = heap;
        this.currentId = incrementID();
        //originalProgram=prg; TODO deepcopy recreate the entire original prg
        stk.push(prg);

    }

    public String fileTableToString() {
        StringBuilder result = new StringBuilder();
        Iterator var2 = this.fileTable.getMap().keySet().iterator();

        while (var2.hasNext()) {
            String filename = (String) var2.next();
            result.append(filename).append("\n");
        }
        return result.toString();
    }

    public PrgState oneStep() throws MyException {
        if (exeStack.isEmpty()) throw new MyException("prgstate stack is empty");
        IStmt crtStmt = exeStack.pop();
        return crtStmt.execute(this);
    }

    public Boolean isNotCompleted() {
        return !exeStack.isEmpty();
    }

    public MyIStack<IStmt> getExeStack() {
        return this.exeStack;
    }

    public MyIDictionary<String, Value> getSymTable() {
        return this.symTable;
    }

    public MyIList<Value> getOut() {
        return this.out;
    }

    public MyIDictionary<String, BufferedReader> getFileTable() {
        return this.fileTable;
    }

    public MyIHeap<Value> getHeap() {
        return this.heap;
    }

    public void setExeStack(MyIStack<IStmt> exeStack) {
        this.exeStack = exeStack;
    }

    public void setSymTable(MyIDictionary<String, Value> symTable) {
        this.symTable = symTable;
    }

    public void setOut(MyIList<Value> out) {
        this.out = out;
    }

    public void setFileTable(MyIDictionary<String, BufferedReader> fileTable) {
        this.fileTable = fileTable;
    }

    public void setHeap(MyIHeap<Value> heap) {
        this.heap = heap;
    }

    @Override
    public String toString() {
        return "PrgState id: " + currentId + " { " + "exeStack=" + exeStack.getReversed() +
                "___symTable=" + symTable + "___fileTable=" + fileTableToString() + "___out=" + out + "}+" +
                "___heap" + heap + "\n";

    }
}
