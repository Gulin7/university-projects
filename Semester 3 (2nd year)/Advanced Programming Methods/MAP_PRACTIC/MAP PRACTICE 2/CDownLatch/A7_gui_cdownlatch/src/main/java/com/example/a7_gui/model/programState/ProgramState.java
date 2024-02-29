package com.example.a7_gui.model.programState;



import com.example.a7_gui.exceptions.*;
import com.example.a7_gui.model.stmt.IStatement;
import com.example.a7_gui.model.utils.*;
import com.example.a7_gui.model.values.Value;

import java.io.BufferedReader;
import java.io.IOException;
import java.util.List;

public class ProgramState {
    private MyIStack<IStatement> exeStack;
    private MyIDictionary<String, Value> symTable;
    private MyIList<Value> out;
    private MyIDictionary<String, BufferedReader> fileTable;
    private MyIHeap heap;
    private MyICountdownLatchTable countdownLatchTable;
    private IStatement originalProgram;
    private int id;
    private static int lastId = 0;

    public ProgramState(MyIStack<IStatement> stack, MyIDictionary<String,Value> symTable, MyIList<Value> out, MyIDictionary<String, BufferedReader> fileTable, MyIHeap heap, MyICountdownLatchTable ctdLatchTbl, IStatement program) {
        this.exeStack = stack;
        this.symTable = symTable;
        this.out = out;
        this.fileTable = fileTable;
        this.heap = heap;
        this.countdownLatchTable = ctdLatchTbl;

        this.originalProgram = program.deepCopy();
        this.exeStack.push(this.originalProgram);
        this.id = setId();
    }

    public ProgramState(MyIStack<IStatement> stack, MyIDictionary<String,Value> symTable, MyIList<Value> out, MyIDictionary<String, BufferedReader> fileTable, MyIHeap heap, MyICountdownLatchTable ctdLatchTbl) {
        this.exeStack = stack;
        this.symTable = symTable;
        this.out = out;
        this.fileTable = fileTable;
        this.heap = heap;
        this.countdownLatchTable = ctdLatchTbl;

        this.id = setId();
    }

    public int getId(){return this.id;}

    public synchronized int setId() {
        lastId++;
        return lastId;
    }

    public void setExeStack(MyIStack<IStatement> newStack) {
        this.exeStack = newStack;
    }

    public void setSymTable(MyIDictionary<String, Value> newSymTable) {
        this.symTable = newSymTable;
    }

    public void setOut(MyIList<Value> newOut) {
        this.out = newOut;
    }

    public void setFileTable(MyIDictionary<String, BufferedReader> newFileTable) {
        this.fileTable = newFileTable;
    }

    public void setHeap(MyIHeap newHeap) {
        this.heap = newHeap;
    }
    public void setCountdownLatchTable(MyICountdownLatchTable newTbl){this.countdownLatchTable = newTbl;}


    public MyIStack<IStatement> getExeStack() {
        return exeStack;
    }

    public MyIDictionary<String, Value> getSymTable() {
        return symTable;
    }

    public MyIList<Value> getOut() {
        return out;
    }

    public MyIDictionary<String, BufferedReader> getFileTable() {
        return fileTable;
    }

    public MyIHeap getHeap() {
        return heap;
    }

    public MyICountdownLatchTable getCountdownLatchTable(){return countdownLatchTable;}

    public boolean isNotCompleted() {
        return exeStack.isEmpty();
    }

    public ProgramState oneStep() throws StatementExecutionException, ADTException, ExpressionEvaluationException, StackException, DivisionByZero {
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

    public String symTableToString() throws ADTException {
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

    public String heapToString() throws ADTException {
        StringBuilder heapStringBuilder = new StringBuilder();
        for (int key: heap.keySet()) {
            heapStringBuilder.append(String.format("%d -> %s\n", key, heap.get(key)));
        }
        return heapStringBuilder.toString();
    }

    public String countDownLatchToString() throws ADTException {
        StringBuilder latchStringBuilder = new StringBuilder();

        for(int key : countdownLatchTable.getCountdownLatchTable().keySet())
            latchStringBuilder.append(String.format("%d -> %d\n", key, countdownLatchTable.get(key)));
        return latchStringBuilder.toString();
    }

    @Override
    public String toString() {
        return "[PROCESS ID]: " + id + "\n[EXE STACK]: \n" + exeStack.getReversed() + "\n[SYMBOL TABLE]: \n" + symTable.toString() + "\n[OUTPUT LIST]: \n" + out.toString() + "\n[FILE TABLE]:\n" + fileTable.toString() + "\n[HEAP STORAGE]:\n" + heap.toString() + "\n" + "\n[LATCHES TABLE]:\n" + countdownLatchTable.toString() + "\n";
    }

    public String programStateToString() throws ADTException {
        return "[PROCESS ID]: " + id + "\n[EXE STACK]: \n" + exeStackToString() + "\n[SYMBOL TABLE]: \n" + symTableToString() + "\n[OUTPUT LIST]: \n" + outToString() + "\n[FILE TABLE]:\n" + fileTableToString() + "\n[HEAP STORAGE]:\n" + heapToString() + "\n[LATCHES TABLE]:\n" + countdownLatchTable.toString();
    }
}