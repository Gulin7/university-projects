package domain.utils;

import exceptions.ListException;

import java.util.ArrayList;
import java.util.List;

public class MyList<T> implements MyIList<T> {
    private final List<T> list;

    public MyList() {
        
        this.list = new ArrayList<T>();
    }

    @Override
    public void add(T itemToAdd) {
        
        this.list.add(itemToAdd);
    }

    @Override
    public void remove(int position) throws ListException {
        if (position >= this.list.size())
            throw new ListException("Invalid index!");

        this.list.remove(position);
    }

    @Override
    public boolean remove(T itemToRemove) {
        return this.list.remove(itemToRemove);
    }

    @Override
    public T getFromPosition(int position) throws ListException {
        if (position >= this.list.size())
            throw new ListException("Invalid index!");

        return this.list.get(position);
    }

    @Override
    public void setValue(int position, T newItem) throws ListException {
        if (position >= this.list.size())
            throw new ListException("Invalid index!");

        this.list.set(position, newItem);
    }

    @Override
    public String toString() {
        return "MyList{ itemsList=" + this.list + "}";
    }
}
