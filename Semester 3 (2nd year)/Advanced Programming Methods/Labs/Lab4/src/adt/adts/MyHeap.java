package adt.adts;

import adt.values.Value;

import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

public class MyHeap implements MyIHeap {
    private final Map<Integer, Value> heapTable;
    private int currentAddress;

    public MyHeap() {
        this.heapTable = new ConcurrentHashMap<>();
        this.currentAddress = 0;
    }

    @Override
    public Map<Integer, Value> getContent() {
        return this.heapTable;
    }

    @Override
    public int getCurrentAddress() {
        return this.currentAddress;
    }

    @Override
    public Value getValueAtAddress(int addressToLook) {
        return this.heapTable.get(addressToLook);
    }

    @Override
    public void updateAddress(Integer addressToUpdate, Value newValue) {
        this.heapTable.put(addressToUpdate, newValue);
    }

    private void incrementAddress() {
        this.currentAddress += 1;
    }

    @Override
    public boolean isDefined(Integer addressToLook) {
        return heapTable.containsKey(addressToLook);
    }

    @Override
    public void setContent(Map<Integer, Value> newHeapValues) {
        this.heapTable.clear();

        for (Integer address : newHeapValues.keySet()) {
            this.heapTable.put(address, newHeapValues.get(address));
        }
    }

    @Override
    public int allocate(Value valueToAllocate) {
        this.incrementAddress();
        this.heapTable.put(this.getCurrentAddress(), valueToAllocate);
        return this.getCurrentAddress();
    }

    @Override
    public String toString() {
        return "MyHeap{" +
                "heapTable=" + heapTable +
                '}';
    }
}