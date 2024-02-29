package com.example.a7_gui.model.programState;



import com.example.a7_gui.exceptions.*;
import com.example.a7_gui.exceptions.ArithmeticException;
import com.example.a7_gui.model.stmt.IStatement;
import com.example.a7_gui.model.utils.*;
import com.example.a7_gui.model.values.Value;

import java.io.BufferedReader;
import java.util.List;

public class ProgramState {
    private MyIStack<IStatement> exeStack;
    private MyIDictionary<String, Value> symTable;
    private MyIList<Value> out;
    private MyIDictionary<String, BufferedReader> fileTable;
    private MyIHeap heap;
    private MyISemaphore semaphoreTable;
    private IStatement originalProgram;
    private int id;
    private static int lastId = 0;

    public ProgramState(MyIStack<IStatement> stack, MyIDictionary<String,Value> symTable, MyIList<Value> out, MyIDictionary<String, BufferedReader> fileTable, MyIHeap heap, MyISemaphore semaphore, IStatement program) {
        this.exeStack = stack;
        this.symTable = symTable;
        this.out = out;
        this.fileTable = fileTable;
        this.heap = heap;
        this.semaphoreTable = semaphore;

        this.originalProgram = program.deepCopy();
        this.exeStack.push(this.originalProgram);
        this.id = setId();
    }

    public ProgramState(MyIStack<IStatement> stack, MyIDictionary<String,Value> symTable, MyIList<Value> out, MyIDictionary<String, BufferedReader> fileTable, MyIHeap heap, MyISemaphore semaphore) {
        this.exeStack = stack;
        this.symTable = symTable;
        this.out = out;
        this.fileTable = fileTable;
        this.heap = heap;
        this.semaphoreTable = semaphore;

        this.id = setId();
    }

    public int getId(){return this.id;}

    public synchronized int setId() {
        lastId++;
        return lastId;
    }

    public MyIStack<IStatement> getExecutionStack() {
        return exeStack;
    }

    public MyIDictionary<String, Value> getSymbolTable() {
        return symTable;
    }

    public MyIList<Value> getOut() {
        return out;
    }

    public MyIDictionary<String, BufferedReader> getFileTable() {
        return fileTable;
    }

    public MyIHeap getHeapTable() {
        return heap;
    }
    public MyISemaphore getSemaphoreTable(){return semaphoreTable;}



    public void setExeStack(MyIStack<IStatement> newStack) {
        this.exeStack = newStack;
    }

    public void setSymbolTable(MyIDictionary<String, Value> newSymTable) {
        this.symTable = newSymTable;
    }

    public void setOut(MyIList<Value> newOut) {
        this.out = newOut;
    }

    public void setFileTable(MyIDictionary<String, BufferedReader> newFileTable) {
        this.fileTable = newFileTable;
    }

    public void setHeapTable(MyIHeap newHeap) {
        this.heap = newHeap;
    }
    public void setSemaphoreTable(MyISemaphore newSemaphore)
    {
        this.semaphoreTable = newSemaphore;
    }

    public boolean isNotCompleted() {
        return exeStack.isEmpty();
    }

    public ProgramState oneStep() throws ExecutionException, DataStructureException, EvaluationException, StackException, ArithmeticException {
        if (exeStack.isEmpty())
            throw new StackException("Program state stack is empty!");
        IStatement currentStatement = exeStack.pop();
        return currentStatement.execute(this);
    }

    public String exeStackToString() {
        StringBuilder exeStackStringBuilder = new StringBuilder();
        List<IStatement> stack = exeStack.getReversed();
        for (IStatement statement: stack) {
            exeStackStringBuilder.append(statement.toString()).append("\n");
        }
        return exeStackStringBuilder.toString();
    }

    public String symTableToString() throws DataStructureException {
        StringBuilder symTableStringBuilder = new StringBuilder();
        for (String key: symTable.keySet()) {
            symTableStringBuilder.append(String.format("%s -> %s\n", key, symTable.lookUp(key).toString()));
        }
        return symTableStringBuilder.toString();
    }

    public String outToString() {
        StringBuilder outStringBuilder = new StringBuilder();
        for (Value elem: out.getList()) {
            outStringBuilder.append(String.format("%s\n", elem.toString()));
        }
        return outStringBuilder.toString();
    }

    public String fileTableToString() {
        StringBuilder fileTableStringBuilder = new StringBuilder();
        for (String key: fileTable.keySet()) {
            fileTableStringBuilder.append(String.format("%s\n", key));
        }
        return fileTableStringBuilder.toString();
    }

    public String heapToString() throws DataStructureException {
        StringBuilder heapStringBuilder = new StringBuilder();
        for (int key: heap.keySet()) {
            heapStringBuilder.append(String.format("%d -> %s\n", key, heap.get(key)));
        }
        return heapStringBuilder.toString();
    }

    public String semaphoreTableToString() throws DataStructureException
    {
        StringBuilder semaphoreTableStringBuilder = new StringBuilder();

        for(int key : semaphoreTable.getSemaphoreTable().keySet())
            semaphoreTableStringBuilder.append(String.format("%d -> (%d, %s)\n", key, semaphoreTable.get(key).getKey(), semaphoreTable.get(key).getValue()));

        return semaphoreTableStringBuilder.toString();
    }

    public String programStateToString() throws DataStructureException {
        return "[PROCESS ID]: " + id + "\n[EXE STACK]: \n" + exeStackToString() + "[SYMBOL TABLE]: \n" + symTableToString() + "[OUTPUT LIST]: \n" + outToString() + "[FILE TABLE]:\n" + fileTableToString() + "[HEAP STORAGE]:\n" + heapToString() + "[SEMAPHORE TABLE]:\n" + semaphoreTableToString();
    }
}