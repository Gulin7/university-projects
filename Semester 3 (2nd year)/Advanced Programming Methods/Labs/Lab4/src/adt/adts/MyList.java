package adt.adts;

import java.util.LinkedList;
import java.util.List;

public class MyList<Type> implements MyIList<Type> {
    private List<Type> output;

    public MyList() {
        output = new LinkedList<>();
    }

    @Override
    public void add(Type e) {
        output.add(e);
    }

    @Override
    public void clear() {
        output.clear();
    }

    @Override
    public String toString() {
        return output.toString();
    }

    public List<Type> getOutput() {
        return output;
    }

    public void setOutput(List<Type> output) {
        this.output = output;
    }
}
