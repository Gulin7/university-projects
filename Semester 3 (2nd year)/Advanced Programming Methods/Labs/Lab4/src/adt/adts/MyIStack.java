package adt.adts;

import java.util.List;

public interface MyIStack<Type> {
    Type pop();
    void push(Type e);

    boolean isEmpty();

    List<Type> getReversed();
}
