package domain.utils;

import exceptions.ListException;
public interface MyIList<T> {
    void add(T itemToAdd);
    void remove(int position) throws ListException;
    boolean remove(T itemToRemove);
    T getFromPosition(int position) throws ListException;
    void setValue(int position, T newItem) throws ListException;
}
