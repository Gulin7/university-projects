package adt;

import adt.adts.*;
import adt.statements.IStmt;
import adt.values.StringValue;
import adt.values.Value;

import java.io.BufferedReader;

public class ProgramState {
    MyIStack<IStmt> executionStack;
    MyIDictionary<String, Value> symbolTable;
    MyIList<Value> outputList;
    MyIDictionary<StringValue, BufferedReader> fileTable;
    private final MyIHeap heapTable;

    public ProgramState(MyIStack<IStmt> stack, MyIDictionary<String,Value> table, MyIList<Value>
            output, MyIDictionary<StringValue, BufferedReader> fileTbl, IStmt program, MyIHeap heapTable){
        executionStack = stack;
        symbolTable = table;
        outputList = output;
        fileTable = fileTbl;
        this.heapTable = heapTable;
        stack.push(program);
    }

    public MyIStack<IStmt> getExecutionStack() {
        return executionStack;
    }

    public void setExecutionStack(MyIStack<IStmt> executionStack) {
        this.executionStack = executionStack;
    }

    public MyIDictionary<String, Value> getSymbolTable() {
        return symbolTable;
    }

    public void setSymbolTable(MyIDictionary<String, Value> symbolTable) {
        this.symbolTable = symbolTable;
    }

    public MyIList<Value> getOutputList() {
        return outputList;
    }

    public void setOutputList(MyIList<Value> outputList) {
        this.outputList = outputList;
    }

    public MyIDictionary<StringValue, BufferedReader> getFileTable() {
        return fileTable;
    }
    public MyIHeap getHeapTable()
    {
        return this.heapTable;
    }

    @Override
    public String toString() {
        return "ProgramState:\n" +
                "executionStack = " + executionStack.getReversed() +
                "\nsymbolTable = " + symbolTable +
                "\noutputList = " + outputList +
                "\n filetable = " + fileTable.getKey();
    }
}
