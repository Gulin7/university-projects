package domain.utils;

import exceptions.StackException;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Stack;

public class MyStack<T> implements MyIStack<T> {

    private final Stack<T> stack;

    public MyStack() { stack = new Stack<T>();}

    @Override
    public T pop() throws StackException {
        if (stack.empty())
            throw new StackException("Empty stack!");

        return stack.pop();
    }

    @Override
    public void push(T itemToPush) {
        stack.push(itemToPush);
    }

    @Override
    public boolean isEmpty() {
        return stack.empty();
    }

    @Override
    public List<T> reverse() {
        ArrayList<T> reverse = new ArrayList<>(stack);

        Collections.reverse(reverse);

        return reverse;
    }
    @Override
    public List<T> getStackAsList() {
        return new ArrayList<>(stack);
    }

    @Override
    public String toString() {
        return "MyStack{ stack= " + this.reverse() + '}';
    }
}
