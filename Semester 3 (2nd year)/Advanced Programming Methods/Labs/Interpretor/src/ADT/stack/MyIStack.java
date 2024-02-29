package ADT.stack;

import java.util.List;
import java.util.Stack;

public interface MyIStack<T> {
    T pop();
    void push(T e);
    boolean isEmpty();
    List<T> getReversed();
    String toString();
    public void setStack();
    Stack<T> getStack();
}
