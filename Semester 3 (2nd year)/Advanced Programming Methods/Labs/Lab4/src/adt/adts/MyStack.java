package adt.adts;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Stack;

public class MyStack<Type> implements MyIStack<Type>{

    Stack<Type> stack;

    public MyStack() {
        this.stack = new Stack<>();
    }

    @Override
    public Type pop() {
        return this.stack.pop();
    }

    @Override
    public void push(Type e) {
        this.stack.push(e);
    }

    @Override
    public boolean isEmpty() {
        return this.stack.isEmpty();
    }

    @Override
    public List<Type> getReversed() {
        List<Type> list = Arrays.asList((Type[]) stack.toArray());
        Collections.reverse(list);
        return  list;
    }

    @Override
    public String toString() {
        return stack.toString();
    }

    public Stack<Type> getStack() {
        return stack;
    }

    public void setStack(Stack<Type> stack) {
        this.stack = stack;
    }
}
